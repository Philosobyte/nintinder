from django.contrib import admin
from .models import User, Game, Interest, Achievement, EarnedAchievement, Event, Participant

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'last_name', 'first_name')
    fields = ['id', ('last_name', 'first_name'), 'email',
              'user_name', 'date_of_birth', 'gender', 'location']


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
