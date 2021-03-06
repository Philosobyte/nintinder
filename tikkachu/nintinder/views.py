import random

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from django.views.generic.edit import CreateView

from .forms import *
from .forms import ProfileForm, UserForm
from .models import Achievement, Friend, Game, User

# Create your views here.

@login_required
def index(request):
    size = User.objects.all().count()
    usr = request.user
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
def games(request):
    user = request.user
    outputArray = user.profile.achievements.all()

    user_games = user.profile.interests.all()
    other_games = (game for game in Game.objects.all() if game not in user_games)

    fullName = user.first_name + ' ' + user.last_name
    currName = user.first_name
    return render(
        request,
        'games.html',
        context={
            'full_name': fullName,
            'name': currName.upper(),
            'user_games': user_games,
            'other_games': other_games
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
    user = requested_user
    profile = user.profile
    currName = user.first_name + ' ' + user.last_name
    currLoc = profile.location
    currBD = profile.date_of_birth
    if not currBD:
        age = 0
    else:
        age = 2018 - currBD.year
    currEmail = user.email

    user_interests = profile.interests.all()
    friends = profile.get_friends()
    user_achievements = profile.achievements.all()

    return render(
        request,
        'profile.html',
        context={
            'user': user,
            'curr': currUser,
            'full_name': currName,
            'location': currLoc,
            'age': age,
            'email': currEmail,
            'usergames': user_interests,
            'userfriends': friends,
            'userachievements': user_achievements,
        },
    )


@login_required
def add_interest(request):
    user = request.user;
    profile = user.profile

    if request.method == 'POST':
        game_id = request.POST.get('gid')
        game = Game.objects.get(id=game_id)
        profile.interests.add(game)
    
    return HttpResponseRedirect(reverse('games'))


@login_required
def achievements(request):
    usr = request.user
    outputArray = usr.profile.achievements.all()

    incompleteArray = list(Achievement.objects.all())
    outArray = incompleteArray[:]
    for z in incompleteArray:
        for i in outputArray:
            if i == z:
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
def earn_achievement(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        achievement_id = request.POST.get('aid')
        achievement = Achievement.objects.get(id=achievement_id)
        profile.achievements.add(achievement)
    
    return HttpResponseRedirect(reverse('achievements'))


@login_required
def settings(request):
    curr_user = request.user
    curr_profile = curr_user.profile
    curr_name = curr_user.first_name + ' ' + curr_user.last_name

    if request.method == 'POST':
        uform = UserForm(request.POST)
        pform = ProfileForm(request.POST)
        if uform.is_valid() and pform.is_valid():
            curr_user.email = uform.clean_email()
            curr_user.first_name = uform.clean_first_name()
            curr_user.last_name = uform.clean_last_name()
            curr_profile.date_of_birth = pform.clean_date_of_birth()
            curr_user.save()
            curr_profile.save()
        return HttpResponseRedirect(reverse('settings'))
    else:
        uform = UserForm(instance=curr_user)
        pform = ProfileForm(instance=curr_profile)
        return render(
            request,
            'settings.html',
            context={
                'usr': curr_user,
                'full_name': curr_name,
                'uform': uform,
                'pform': pform
            },
        )


matches = []
pending_other_initiated = []

@login_required
def matches(request):
    curr_user = request.user
    curr_name = curr_user.first_name + ' ' + curr_user.last_name
    curr_profile = curr_user.profile

    global matches
    global pending_other_initiated

    if request.method == 'GET':
        # Set of Profiles which added the current user as a friend but the current user has not responded
        pending_other_initiated = \
            {friend.friendA for friend in Friend.objects.filter(friendB=curr_profile, status=Friend.STATUS_PENDING)}

        # Set of Profiles which the current user added as friends but have not responded
        pending_curr_initiated = \
            {friend.friendB for friend in Friend.objects.filter(friendA=curr_profile, status=Friend.STATUS_PENDING)}

        # QuerySet of  Friend objects containing the current user and are labeled as blacklisted
        temp_blacklist = \
            Friend.objects.filter(Q(friendA=curr_profile) | Q(friendB=curr_profile), status=Friend.STATUS_BLACKLIST)

        # QuerySet of Friend objects containing the current user and are labeled as friends
        temp_already_friends = \
            Friend.objects.filter(Q(friendA=curr_profile) | Q(friendB=curr_profile), status=Friend.STATUS_FRIEND)

        # Set of Profiles which blacklisted the current user or which the current user blacklisted
        blacklist = set()

        # Set of Profiles which are already friends with the current user
        already_friends = set()

        # Set of Profiles with at least one game/interest in common with the current user
        profiles_same_interests = set()

        # The final list of profiles to present to the current user for adding or ignoring
        matches = []

        # A dictionary {Profile: {Game}} which specifies which games a certain Profile is interested in.
        interests = {}

        for friend in temp_blacklist:
            blacklist.add(friend.friendA)
            blacklist.add(friend.friendB)

        for friend in temp_already_friends:
            already_friends.add(friend.friendA)
            already_friends.add(friend.friendB)

        for game in curr_profile.interests.all():
            profiles_same_interests.update(game.profile_set.all())

        matches = list((pending_other_initiated | profiles_same_interests)
                       - blacklist - pending_curr_initiated - already_friends - {curr_profile})

        for profile in matches:
            interests[profile] = list(profile.interests.all())
        print('buddies of curr_user: {}'.format(curr_profile.buddies.all()))
        return render(
            request,
            'matches.html',
            context={
                'full_name': curr_name,
                'friends': matches,
                'people': len(matches),
                'range': [] if len(matches) == 0 else [str(i) for i in range(len(matches))],
                'interests': interests,
            },
        )
    if request.method == 'POST':
        index = request.POST['index']
        other = matches[int(index)]
        if 'Add Friend' in request.POST:
            print('entered Add Friend')
            curr_profile.add_friend(other)
        elif 'Ignore' in request.POST:
            print('entered Ignore')
            curr_profile.blacklist_friend(other)
        return HttpResponseRedirect(reverse('matches'))


def login(request):
  return render(
      request,
      'login.html',
  )

def sign_up(request):
  if request.method == 'POST':
    print(request.POST['first_name'])
    print(request.POST['last_name'])
    print(request.POST['username'])
    print(request.POST['email'])
    print(request.POST['password1'])
    print(request.POST['password2'])
    form = SignUpForm(request.POST)
    if form.is_valid():
      print("form is valid")
      form.save()
      messages.success(request, 'Account created successfully')
      return HttpResponseRedirect('/')
    else:
      form = SignUpForm()
  return render(
      request,
      'sign_up.html',
  )
