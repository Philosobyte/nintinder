import random
from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ProfileForm, UserForm
# Create your views here.
from .models import (Achievement, EarnedAchievement, Event, Friend, Game,
                     Interest, Participant, Profile, User)


@login_required
def index(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)]
    currName = usr.first_name + ' ' + usr.last_name
    games = Game.objects.all()
    rand = random.randint(0, games.count() - 1)
    gCurr = games[rand].name
    gNext = games[(rand+3) % (games.count() - 1)].name
    return render(
        request,
        'index.html',
        context={
            'full_name': currName,
            'game1': gCurr,
            'game2': gNext,
        },
    )


@login_required
def profile(request):
    size = User.objects.all().count()
    currUser = request.user.first_name
    usr = request.user
    profile = usr.profile
    currName = usr.first_name + ' ' + usr.last_name
    currLoc = profile.location
    currBD = profile.date_of_birth
    if not currBD:
        age = 0
    else:
        age = 2018 - currBD.year
    currEmail = usr.email

    size = Game.objects.all().count()
    seed = random.randint(0, size - 1)
    gameArray = Game.objects.all()
    gameTuple = (gameArray[seed].name, gameArray[(seed + 1) % size].name, gameArray[(seed - 1) % size].name)

    return render(
        request,
        'profile.html',
        context={
            'curr': currUser,
            'full_name': currName,
            'location': currLoc,
            'age': age,
            'email': currEmail,
            'gTuple': gameTuple
        },
    )


@login_required
def achievements(request):
    usr = request.user
    outputArray = EarnedAchievement.objects.filter(user=usr)

    incompleteArray = list(Achievement.objects.all())
    outArray = incompleteArray[:]
    for z in incompleteArray:
        for i in outputArray:
            if i.achievement == z:
                outArray.remove(z)
    fullName = usr.first_name + ' ' + usr.last_name
    currName = usr.first_name
    return render(
        request,
        'achievements.html',
        context={
            'full_name': fullName,
            'name': currName.upper(),
            'complete': outputArray,
            'incomplete': outArray
        },
    )


@login_required
def settings(request):
    usr = request.user
    profile = usr.profile
    currName = usr.first_name + ' ' + usr.last_name

    if request.method == 'POST':
        uform = UserForm(request.POST)
        pform = ProfileForm(request.POST)
        if uform.is_valid() and pform.is_valid():
            usr.email = uform.clean_email()
            usr.first_name = uform.clean_first_name()
            usr.last_name = uform.clean_last_name()
            profile.date_of_birth = pform.clean_date_of_birth()
            usr.save()
            profile.save()
        return HttpResponseRedirect(reverse('settings'))
    else:
        uform = UserForm(instance=usr)
        pform = ProfileForm(instance=profile)
        return render(
            request,
            'settings.html',
            context={
                'full_name': currName,
                'uform': uform,
                'pform': pform
            },
        )


@login_required
def matches(request):
    usr = request.user
    currName = usr.first_name + ' ' + usr.last_name

    friendsArray = Friend.objects.filter((Q(friendA=usr) | Q(friendB=usr)), status=0)

    outputArray = [(x.friendA if (x.friendB == usr) else x.friendB) for x in friendsArray]

    friends_qs = Q( user=None )
    for friend in outputArray:
        friends_qs = friends_qs | Q(user=friend)
    interestsArray = Interest.objects.filter(friends_qs)

    interests = defaultdict(list)
    for x in interestsArray:
        interests[x.user].append(x.game)

    return render(
        request,
        'matches.html',
        context={
            'full_name': currName,
            'friends': outputArray,
            'people': len(outputArray),
            'interests': interests,
        },
    )


def login(request):
    return render(
        request,
        'login.html',
        context={
            'user': usr,
        },
    )
