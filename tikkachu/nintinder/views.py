from django.shortcuts import render

# Create your views here.
from .models import User, Game, Interest, Achievement, EarnedAchievement, Event, Participant, Friend

def index(request):
    usr = User.objects.all()[0] #For testing/database purposes, just picking the first User object made and taking their first/last name to use for the Profile right now
    currName = usr.first_name + ' ' + usr.last_name
    return render(
        request,
        'index.html',
        context={
            'full_name': currName
        },
    )