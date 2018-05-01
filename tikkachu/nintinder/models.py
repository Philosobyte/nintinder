import uuid

from django.contrib.auth.models import User
from django.db import NotSupportedError, models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaulttags import register
from django.db.models import Q


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
    interests = models.ManyToManyField(Game, blank=True)
    achievements = models.ManyToManyField(Achievement, blank=True)
    bio = models.CharField(max_length=1024, blank=True, help_text="Enter the user's bio")
    title = models.CharField(max_length=64, default="Player", help_text="Enter the user's title")

    buddies = models.ManyToManyField('self', through='Friend', related_name='friends+', symmetrical=False, blank=True)

    def get_friends(self, status=0):
        temp_friends = Friend.objects.filter(Q(friendA=self) | Q(friendB=self), status=status)
        compadres = set()
        for friend in temp_friends:
            compadres.add(friend.friendA)
            compadres.add(friend.friendB)

        return compadres - {self}

    def add_friend(self, friend):
        """
        Friendship is not symmetrical. If
        """
        print('friend: {}'.format(friend))
        # prevent users from befriending themselves
        if self == friend:
            raise NotSupportedError("Cannot befriend one's self")

        ab, ab_created = Friend.objects.get_or_create(
            friendA=self,
            friendB=friend
        )
        ba, ba_created = Friend.objects.get_or_create(
            friendA=friend,
            friendB=self
        )
        if ab_created and ba_created:
            ab.status = Friend.STATUS_PENDING
            ab.save()
            ba.delete()
        elif not ba_created:
            if ba.status == Friend.STATUS_PENDING:
                ba.status = Friend.STATUS_FRIEND
                ba.save()
                ab.delete()

    def blacklist_friend(self, friend):
        self.remove_friend(friend)
        friendship, created = Friend.objects.get_or_create(
            # if blacklisting then requesting friendA is self 
            friendA=self,
            friendB=friend
        )
        friendship.status = Friend.STATUS_BLACKLIST
        friendship.save()

    def remove_friend(self, friend):
        Friend.objects.filter(Q(friendA=self, friendB=friend)|Q(friendA=friend, friendB=self)).delete()

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


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
    friendA = models.ForeignKey(Profile, related_name='friendA', on_delete=models.CASCADE, help_text="Enter the id of the user to whom this friends list belongs")
    friendB = models.ForeignKey(Profile, related_name='friendB', on_delete=models.CASCADE, help_text="Enter the id of the user who is on the friends list")

    STATUS_FRIEND = 0
    STATUS_PENDING = 1
    STATUS_BLACKLIST = 2

    STATUSES = (
        (STATUS_FRIEND, u'friends'),
        (STATUS_PENDING, u'pending'),
        (STATUS_BLACKLIST, u'blacklist'),
    )

    status = models.SmallIntegerField(choices=STATUSES, blank=True, null=True)

    class Meta:
        unique_together = (('friendA', 'friendB'),)

    def __str__(self):
        if self.status == '0':
            status = 'friends'
        elif self.status == '1':
            status = 'pending'
        else:
            status = 'not right for each other'

        return "{} and {} are {}".format(self.friendA, self.friendB, status)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
