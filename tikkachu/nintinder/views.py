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

from .forms import ProfileForm, UserForm
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

friendsArray = None
friendAArray = None
outputArray = None


@login_required
def matches(request):
    MAX_MATCHES = 10
    usr = request.user
    currName = usr.first_name + ' ' + usr.last_name
    global friendsArray
    global friendAArray
    global outputArray
    if request.method == 'GET':
        friendsArray = Friend.objects.filter(Q(friendB=usr), status=1)
        pendingFriendsArray = Friend.objects.filter(Q(friendA=usr), status=1)
        print('pendingFriendsArray: {}'.format(pendingFriendsArray))
        pendingArray = [friend.friendB for friend in pendingFriendsArray]
        print('pendingArray: {}'.format(pendingArray))
        outputArray = [friend.friendA for friend in friendsArray]
        friendAArray = list(outputArray)
        blacklisted = set()
        for friend in Friend.objects.filter(Q(friendA=usr)|Q(friendB=usr), status=4):
            blacklisted.add(friend.friendA)
            blacklisted.add(friend.friendB)
        curr_user_games = {interest.game for interest in Interest.objects.filter(Q(user=usr))}

        for curr_game in curr_user_games:
            interests_with_game = Interest.objects.filter(Q(game=curr_game))
            for interest in interests_with_game:
                print('length of outputArray: {}'.format(len(outputArray)))
                if interest.user != usr and interest.user not in outputArray and interest.user not in pendingArray \
                        and interest.user not in blacklisted:
                    outputArray.append(interest.user)

        interests = defaultdict(list)
        for user in outputArray:
            interest_array = Interest.objects.filter(Q(user=user))
            for interest in interest_array:
                interests[user].append(interest.game)
        print([str(i) for i in range(len(outputArray))])
        return render(
            request,
            'matches.html',
            context={
                'full_name': currName,
                'friends': outputArray,
                'people': len(outputArray),
                'range': [] if len(outputArray) == 0 else [str(i) for i in range(len(outputArray))],
                'interests': interests,
            },
        )

    if request.method == 'POST':
        index = request.POST['index']
        other = outputArray[int(index)]
        print('request.POST: {}'.format(request.POST))
        print('outputArray: {}'.format(outputArray))
        print('index: {}'.format(index))
        print('other: {}'.format(other))
        print('friendAArray: {}'.format(friendAArray))
        print('friendsArray: {}'.format(friendsArray))
        if other in friendAArray:
            for friend in friendsArray:
                if friend.friendA == other:
                    if 'Add Friend' in request.POST:
                        friend.status = u'0'
                    else:
                        friend.status = u'4'
                    friend.save()
        else:
            if 'Add Friend' in request.POST:
                friend = Friend(friendA=usr, friendB=other, status=u'1')
            else:
                friend = Friend(friendA=usr, friendB=other, status=u'4')
            friend.save()
        return HttpResponseRedirect(reverse('matches'))


def login(request):
    return render(
        request,
        'login.html',
    )
