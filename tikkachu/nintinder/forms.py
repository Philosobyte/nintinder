from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from .models import Game, Profile
from django.contrib.auth.models import User as django_user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        labels = {'email': 'Email', 'first_name': 'First Name', 'last_name': 'Last Name'}

    def clean_email(self):
        data = self.cleaned_data['email']
        return data

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        return data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth']
        labels = {'date_of_birth': 'Date of Birth'}

    def clean_date_of_birth(self):
        data = self.cleaned_data['date_of_birth']
        return data
                


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


class FriendForm(forms.Form):
    user_choices = (('A', 'Add'), ('B', "Ignore"))
    friend_choice = forms.MultipleChoiceField(choices=user_choices)

    def clean_friend_choice(self):
        data = self.cleaned_data['friend_choice']
        return data

class SignUpForm(forms.ModelForm):
  class Meta:
    model = django_user
    fields = ['username', 'first_name', 'last_name', 'password', 'email']
    