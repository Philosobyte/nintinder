import random
from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import *
# Create your views here.
from .models import (Achievement, Event, Friend, Game, Participant,
                     Profile, User)

# Right now, we have the home page assuming ANY of the multiple users in the database are logged on, and randomly picks one, 
# For the actual website, obviously we would be getting a static user and their static friends 


# class InterestCreate(CreateView):
#     model = Interest
#     fields = {'game'}
#     success_url = reverse_lazy('profile')
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(InterestCreate, self).form_valid(form)


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

    # incompleteArray = list(Achievement.objects.all())
    # outArray = incompleteArray[:]
    # for z in incompleteArray:
    #     for i in outputArray:
    #         if i == z:
    #             outArray.remove(z)
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
def get_friends(request):
    user = request.user
    profile = user.profile

    if request.method == 'GET':
        output = {}

        for status in [Friend.STATUS_FRIEND, Friend.STATUS_PENDING, Friend.STATUS_BLACKLIST]:
            data = {}
            friends = profile.get_friends(status)
            
            usernames = [ friend.user.username for friend in friends ]
            data[user.username] = usernames

            for friend in friends:
                data[friend.user.username] = [ buddy.friendB.user.username for buddy in friend.friendA.get_friends(status) ]

            output[status] = data

    return JsonResponse(output, safe=False)


@login_required
def add_friend(request):
    user = request.user
    profile = user.profile

    if request.method == 'GET':
        other = request.GET.get('username')
        friend = User.objects.get(username=other)
        profile.add_friend(friend.profile)

    return HttpResponseRedirect(reverse('get_friends'))


@login_required
def remove_friend(request):
    user = request.user
    profile = user.profile

    if request.method == 'GET':
        other = request.GET.get('username')
        ex = User.objects.get(username=other)
        profile.remove_friend(ex.profile)

    return HttpResponseRedirect(reverse('get_friends'))


@login_required
def blacklist_friend(request):
    user = request.user
    profile = user.profile

    if request.method == 'GET':
        other = request.GET.get('username')
        ex = User.objects.get(username=other)
        profile.blacklist_friend(ex.profile)

    return HttpResponseRedirect(reverse('get_friends'))


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
        pending_other_initiated = {friend.friendA for friend in Friend.objects.filter(friendB=curr_profile, status=1)}
        pending_curr_initiated = {friend.friendB for friend in Friend.objects.filter(friendA=curr_profile, status=1)}
        temp_blacklist = Friend.objects.filter(Q(friendA=curr_profile) | Q(friendB=curr_profile), status=2)
        blacklist = set()
        for friend in temp_blacklist:
            blacklist.add(friend.friendA)
            blacklist.add(friend.friendB)
        profiles_same_interests = set()
        for game in curr_profile.interests.all():
            profiles_same_interests.update(game.profile_set.all())

        matches = list(pending_other_initiated | profiles_same_interests
                       - blacklist - pending_curr_initiated - {curr_profile})
        interests = {}
        for profile in matches:
            interests[profile] = list(profile.interests.all())
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