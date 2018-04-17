from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import Profile, Game


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

class GameForm(forms.Form):
    list_games = Game.objects.all()
    list_platforms = []
    for obj in list_games:
        list_platforms.append(obj.platform)
    unique_platforms = set(list_platforms)
        
    game_title = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Game Title'}))
    size = len(unique_platforms)
    game_platform = forms.ChoiceField(choices = [(list(range(1,size)), unique_platforms)])
    game_publisher = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Game Publisher'}))
    game_release_date = forms.TimeField(widget= forms.TimeInput(format= '%Y-%m-%d'))
    game_description = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Game Description'}))

    class Meta:
        model = Game
