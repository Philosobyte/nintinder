from django.db import models
from django.template.defaulttags import register
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
import datetime
import uuid

from django.urls import reverse
# Create your models here.

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=128, help_text="Enter the name of the game")
    platform = models.CharField(max_length=32, help_text="Enter the game's platform")
    publisher = models.CharField(max_length=32, help_text="Enter the game's publisher")
    release_date = models.DateField(null=True, blank=True, help_text="Enter the game's release date")
    description = models.CharField(max_length=1024, help_text="Enter a description of the game")

    def __str__(self):
        return "{} for {}".format(self.name, self.platform)


class Interest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the username of the user who is interested in a game")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text="Enter the game the user is interested in")

    def __str__(self):
        return "{} is interested in {}".format(self.user, self.game)

    class Meta:
        unique_together = (('user', 'game'),)


class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text="Enter the game's id")
    name = models.CharField(max_length=128, help_text="Enter the name of the achievement in the game")

    def __str__(self):
        return "{} in {}".format(self.name, self.game)
    def get_absolute_url(self):
        return u'/nintinder/achievements/'


class Profile(models.Model):
    """
    Model representing a user of the service
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=256, help_text="Enter the user's location")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Enter the user's date of birth")
    interests = models.ManyToManyField(Game)
    achievements = models.ManyToManyField(Achievement)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class EarnedAchievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the username of the user who has earned the achievement")
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, help_text="Enter id of the achievement they earned")

    def __str__(self):
        return "{} has completed {}".format(self.user, self.achievement)


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text="Enter the name of the game")
    start_time = models.DateTimeField(null=True, blank=True, help_text="Enter the start time of the event")
    end_time = models.DateTimeField(null=True, blank=True, help_text="Enter the end time of the event (blank if still ongoing")

    def __str__(self):
        return "{} from {} to {}".format(self.game, self.start_time,
                                         self.end_time if self.end_time is not None else 'present')


class Participant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, help_text="Enter the id of the event")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the id of user participating in the event")
    start_time = models.DateTimeField(null=True, blank=True, help_text="Enter when the user started participating in the event")
    end_time = models.DateTimeField(null=True, blank=True, help_text="Enter when the user finished participating in the event (blank if ongoing)")

    def __str__(self):
        return "{} at {}".format(self.user, self.event)


class Friend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    friendA = models.ForeignKey(User, related_name='friendA', on_delete=models.CASCADE, help_text="Enter the id of the user to whom this friends list belongs")
    friendB = models.ForeignKey(User, related_name='friendB', on_delete=models.CASCADE, help_text="Enter the id of the user who is on the friends list")

    STATUSES = (
        (u'0', u'friends'),
        (u'1', u'pending'),
        (u'2', u'blacklistAB'),
        (u'3', u'blacklistBA'),
        (u'4', u'blacklist'),
    )

    status = models.CharField(max_length=1, choices=STATUSES)

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    def __str__(self):
        if self.status == '0':
            status = 'friends'
        elif self.status == '1':
            status = 'pending'
        else:
            status = 'not right for each other'

        return "{} and {} are {}".format(self.friendA, self.friendB, status)
