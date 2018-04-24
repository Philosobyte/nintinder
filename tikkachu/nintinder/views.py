import random
from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.edit import CreateView

from .forms import ProfileForm, UserForm
# Create your views here.
from .models import (Achievement, EarnedAchievement, Event, Friend, Game,
                     Interest, Participant, Profile, User)

# Right now, we have the home page assuming ANY of the multiple users in the database are logged on, and randomly picks one, 
# For the actual website, obviously we would be getting a static user and their static friends 


class InterestCreate(CreateView):
    model = Interest
    fields = {'game'}
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InterestCreate, self).form_valid(form)
    

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
def profile(request, user_profile=None):
    requested_user = None
    if user_profile is None:
      requested_user = request.user
    else:
      user_profile_name = user_profile.split(' ')
      user_query = User.objects.all().filter(first_name=user_profile_name[0])
      requested_user = user_query[0]

    currUser = requested_user.first_name
    usr = requested_user
    profile = usr.profile
    currName = usr.first_name + ' ' + usr.last_name
    currLoc = profile.location
    currBD = profile.date_of_birth
    if not currBD:
        age = 0
    else:
        age = 2018 - currBD.year
    currEmail = usr.email

    userinterests = Interest.objects.filter(user=usr)
    gamelist=[]
    for interest in userinterests:
        gamelist.append(interest.game)

    userfriends = Friend.objects.filter((Q(friendA=usr) | Q(friendB=usr)), status=0)
    friendlist=[]
    for friend in userfriends:
        if friend.friendA == usr:
            friendlist.append(friend.friendB)
        elif friend.friendB == usr:
            friendlist.append(friend.friendA)

    usercahievs = EarnedAchievement.objects.filter(user=usr)
    achievlist=[]
    for achiev in usercahievs:
        achievlist.append(achiev.achievement)

    return render(
        request,
        'profile.html',
        context={
            'usr': usr,
            'curr': currUser,
            'full_name': currName,
            'location': currLoc,
            'age': age,
            'email' : currEmail,
            'usergames': gamelist,
            'userfriends': friendlist,
            'userachievements': achievlist,
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
                'usr': usr,
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
    )
