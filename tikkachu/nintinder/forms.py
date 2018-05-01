from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput, TextInput

from .models import Game, Profile


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

class SuperCustomAuthForm(forms.Form):
    email = forms.CharField(widget=TextInput(attrs={'placeholder':'Email'}))


class FriendForm(forms.Form):
    user_choices = (('A', 'Add'), ('B', "Ignore"))
    friend_choice = forms.MultipleChoiceField(choices=user_choices)

    def clean_friend_choice(self):
        data = self.cleaned_data['friend_choice']
        return data

class SignUpForm(forms.Form):
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    username = forms.CharField(min_length=4, max_length=150)
    email = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_first_name(self):
        pass
    def clean_last_name(self):
        pass

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        check_existence = User.objects.filter(username=username)
        if check_existence.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        check_existence = User.objects.filter(email=email)
        if check_existence.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match.")

        return password2

    def save(self, commit=True):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        user = User.objects.create_user(
            username,
            email,
            password
        )
        return user
