from django.shortcuts import render
import random


# Right now, we have the home page assuming ANY of the multiple users in the database are logged on, and randomly picks one, 
# For the actual website, obviously we would be getting a static user and their static friends 

# Create your views here.
from .models import User, Game, Interest, Achievement, EarnedAchievement, Event, Participant, Friend

def index(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    currName = usr.first_name + ' ' + usr.last_name
    return render(
        request,
        'index.html',
        context={
            'full_name': currName
        },
    )

def profile(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    currName = usr.first_name + ' ' + usr.last_name
    currLoc = usr.location
    currBD = usr.date_of_birth
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
    completedArray = list(EarnedAchievement.objects.all())
    outputArray = completedArray[:]
    for x in completedArray:
        if x.user != usr:
            outputArray.remove(x)
    incompleteArray = list(Achievement.objects.all())
    outArray = incompleteArray[:]
    for z in incompleteArray:
        for i in outputArray:
            if i.achievement == z:
                outArray.remove(z)
                
    currName = usr.first_name
    return render(
        request,
        'achievements.html',
        context={
            'name': currName.upper(),
            'complete': outputArray,
            'incomplete': outArray
        },
    )
    
def settings(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    currName = usr.first_name + ' ' + usr.last_name
    firstName = usr.first_name
    lastName = usr.last_name
    date_of_birth = usr.date_of_birth
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
    return render(
        request,
        'matches.html',
        context={
            'full_name': currName
        },
    )
