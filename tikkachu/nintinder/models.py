from django.db import models
import datetime
import uuid

# Create your models here.


class User(models.Model):
    """
    Model representing a user of the service
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=64, help_text="Enter a username")
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    location = models.CharField(max_length=256)
    dateOfBirth = models.DateField(auto_now_add=True)
    gender = models.SmallIntegerField()
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.username


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=128)
    platform = models.CharField(max_length=32)
    publisher = models.CharField(max_length=32)
    releaseDate = models.DateField(auto_now_add=False)
    description = models.CharField(max_length=1024)


class Interest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'game'),)


class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)


class EarnedAchievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achieve = models.ForeignKey(Achievement, on_delete=models.CASCADE)


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(blank=True)


class Participant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(blank=True)
