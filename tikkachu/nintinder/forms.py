from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms.widgets import TextInput


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        labels = {'email': 'Email', 'first_name': 'First Name', 'last_name': 'Last Name'}
        #widgets = {'email': TextInput(attrs={'placeholder': 'name', 'class': 'ui'})}

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