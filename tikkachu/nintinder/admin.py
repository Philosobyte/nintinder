from django.contrib import admin
from .models import Profile, Game, Interest, Achievement, EarnedAchievement, Event, Participant, Friend

# Register your models here.

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'location')
    fields = ['user', 'date_of_birth', 'location']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'release_date')


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'game')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'name')


@admin.register(EarnedAchievement)
class EarnedAchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'achievement')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'start_time', 'end_time')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'user')


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'friendA', 'friendB', 'status')
