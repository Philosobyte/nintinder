from django.contrib import admin
from .models import User, Game, Interest, Achievement, EarnedAchievement, Event, Participant

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_name', 'first_name')
    fields = [('last_name', 'first_name'), 'email', 'username', 'date_of_birth', 'gender']
