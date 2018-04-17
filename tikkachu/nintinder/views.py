from django.db.models import Q
from django.shortcuts import render
from collections import defaultdict
import random


# Right now, we have the home page assuming ANY of the multiple users in the database are logged on, and randomly picks one, 
# For the actual website, obviously we would be getting a static user and their static friends 

# Create your views here.
from .models import User, Game, Interest, Achievement, EarnedAchievement, Event, Participant, Friend, Profile

def index(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
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
            'game1' : gCurr, 
            'game2' : gNext,
        },
    )

def profile(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    profile = usr.profile
    currName = usr.first_name + ' ' + usr.last_name
    currLoc = profile.location
    currBD = profile.date_of_birth
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
            'full_name': currName,
            'location': currLoc,
            'age': age,
            'email' : currEmail,
            'gTuple': gameTuple
        },
    )

def achievements(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)]
     #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    # completedArray = list(EarnedAchievement.objects.all())
    outputArray = EarnedAchievement.objects.filter( user=usr )
    # for x in completedArray:
    #     if x.user != usr:
    #         outputArray.remove(x)
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
    
def settings(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    profile = usr.profile
    currName = usr.first_name + ' ' + usr.last_name
    firstName = usr.first_name
    lastName = usr.last_name
    date_of_birth = profile.date_of_birth
    email = usr.email
    return render(
        request,
        'settings.html',
        context={
            'full_name': currName,
            'first_name': firstName,
            'last_name' : lastName,
            'DOB': date_of_birth,
            'email': email
        },
    )
    
def matches(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    currName = usr.first_name + ' ' + usr.last_name

    # friendsArray = list(Friend.objects.all())
    friendsArray = Friend.objects.filter((Q(friendA=usr) | Q(friendB=usr)), status=0)
    # friendsArray = list(friendsArray)

    outputArray = [(x.friendA if (x.friendB == usr) else x.friendB) for x in friendsArray]
    # outputArray = list(outputArray)
    # outputArray = []
    # for x in friendsArray:
    #     if ((x.friendA == usr) or (x.friendB == usr)) and x.status == '0':
    #        outputArray.append(x.friendA if (x.friendB == usr) else x.friendB)

    # interestsArray = list(Interest.objects.all())
    friends_qs = Q( user=None )
    for friend in outputArray:
        friends_qs = friends_qs | Q(user=friend)
    interestsArray = Interest.objects.filter(friends_qs)
    # interestsArray = list(interestsArray)

    outputDict2 = defaultdict(list)
    for x in interestsArray:
        outputDict2[x.user].append(x.game)

    # outputDict2 = { x.user:  }

    return render(
        request,
        'matches.html',
        context={
            'full_name': currName,
            'friends': outputArray,
            'people': len(outputArray),
            'interests': outputDict2,
        },
    )
