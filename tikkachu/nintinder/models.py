from django.db import models
import datetime
import uuid

# Create your models here.


class User(models.Model):
    """
    Model representing a user of the service
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_name = models.CharField(max_length=64, help_text="Enter a username")
    first_name = models.CharField(max_length=64, help_text="Enter the user's first name")
    last_name = models.CharField(max_length=64, help_text="Enter the user's last name")
    location = models.CharField(max_length=256, help_text="Enter the user's location")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Enter the user's date of birth")
    gender = models.SmallIntegerField(null=True, blank=True, help_text="Enter the user's gender")
    email = models.CharField(max_length=256, help_text="Enter the user's email address")

    def __str__(self):
        return self.user_name


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=128, help_text="Enter the name of the game")
    platform = models.CharField(max_length=32, help_text="Enter the game's platform")
    publisher = models.CharField(max_length=32, help_text="Enter the game's publisher")
    release_date = models.DateField(null=True, blank=True, help_text="Enter the game's release date")
    description = models.CharField(max_length=1024, help_text="Enter a description of the game")

    def __str__(self):
        return "%s for %s" % (self.name, self.platform)


class Interest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the username of the user who is interested in a game")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text="Enter the game the user is interested in")

    class Meta:
        unique_together = (('user', 'game'),)


class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text="Enter the game's id")
    name = models.CharField(max_length=128, help_text="Enter the name of the achievement in the game")


class EarnedAchievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the username of the user who has earned the achievement")
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, help_text="Enter id of the achievement they earned")


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text="Enter the name of the event")
    start_time = models.DateTimeField(null=True, blank=True, help_text="Enter the start time of the event")
    end_time = models.DateTimeField(null=True, blank=True, help_text="Enter the end time of the event (blank if still ongoing")


class Participant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, help_text="Enter the id of the event")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the id of user participating in the event")
    start_time = models.DateTimeField(null=True, blank=True, help_text="Enter when the user started participating in the event")
    end_time = models.DateTimeField(null=True, blank=True, help_text="Enter when the user finished participating in the event (blank if ongoing)")

class Friend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the id of the user to whom this friends list belongs")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the id of the user who is on the friends list")

class BlackList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the id of the user to whom this blacklist belongs")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Enter the id of the user who is on the blacklist")
