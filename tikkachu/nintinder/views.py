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
    return render(
        request,
        'profile.html',
        context={
            'full_name': currName
        },
    )

def achievements(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    currName = usr.first_name + ' ' + usr.last_name
    return render(
        request,
        'achievements.html',
        context={
            'full_name': currName
        },
    )
    
def settings(request):
    size = User.objects.all().count()
    usr = User.objects.all()[random.randint(0, size - 1)] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    currName = usr.first_name + ' ' + usr.last_name
    return render(
        request,
        'settings.html',
        context={
            'full_name': currName
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
