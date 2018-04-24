from django.contrib import admin
from .models import Profile, Game, Interest, Achievement, Event, Participant, Friend

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'location', 'bio', 'title')
    fields = ['user', 'date_of_birth', 'location', 'interests', 'achievements', 'bio', 'title']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'release_date', 'id')


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'game')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'name')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'start_time', 'end_time')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'user')


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'friendA', 'friendB', 'status')
