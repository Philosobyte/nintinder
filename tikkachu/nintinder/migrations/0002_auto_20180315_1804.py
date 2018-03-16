# Generated by Django 2.0.2 on 2018-03-15 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nintinder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='game',
            field=models.ForeignKey(help_text="Enter the game's id", on_delete=django.db.models.deletion.CASCADE, to='nintinder.Game'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='name',
            field=models.CharField(help_text='Enter the name of the achievement in the game', max_length=128),
        ),
        migrations.AlterField(
            model_name='earnedachievement',
            name='achieve',
            field=models.ForeignKey(help_text='Enter id of the achievement they earned', on_delete=django.db.models.deletion.CASCADE, to='nintinder.Achievement'),
        ),
        migrations.AlterField(
            model_name='earnedachievement',
            name='user',
            field=models.ForeignKey(help_text='Enter the username of the user who has earned the achievement', on_delete=django.db.models.deletion.CASCADE, to='nintinder.User'),
        ),
        migrations.AlterField(
            model_name='event',
            name='endTime',
            field=models.DateTimeField(blank=True, help_text='Enter the end time of the event (blank if still ongoing'),
        ),
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.ForeignKey(help_text='Enter the name of the event', on_delete=django.db.models.deletion.CASCADE, to='nintinder.Game'),
        ),
        migrations.AlterField(
            model_name='event',
            name='startTime',
            field=models.DateTimeField(auto_now_add=True, help_text='Enter the start time of the event'),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(help_text='Enter a description of the game', max_length=1024),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(help_text='Enter the name of the game', max_length=128),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.CharField(help_text="Enter the game's platform", max_length=32),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(help_text="Enter the game's publisher", max_length=32),
        ),
        migrations.AlterField(
            model_name='game',
            name='releaseDate',
            field=models.DateField(help_text="Enter the game's release date"),
        ),
        migrations.AlterField(
            model_name='interest',
            name='game',
            field=models.ForeignKey(help_text='Enter the game the user is interested in', on_delete=django.db.models.deletion.CASCADE, to='nintinder.Game'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='user',
            field=models.ForeignKey(help_text='Enter the username of the user who is interested in a game', on_delete=django.db.models.deletion.CASCADE, to='nintinder.User'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='endTime',
            field=models.DateTimeField(blank=True, help_text='Enter when the user finished participating in the event (blank if ongoing)'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='event',
            field=models.ForeignKey(help_text='Enter the id of the event', on_delete=django.db.models.deletion.CASCADE, to='nintinder.Event'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='startTime',
            field=models.DateTimeField(auto_now_add=True, help_text='Enter when the user started participating in the event'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(help_text='Enter the id of user participating in the event', on_delete=django.db.models.deletion.CASCADE, to='nintinder.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dateOfBirth',
            field=models.DateField(auto_now_add=True, help_text="Enter the user's date of birth"),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(help_text="Enter the user's email address", max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(help_text="Enter the user's first name", max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.SmallIntegerField(help_text="Enter the user's gender"),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(help_text="Enter the user's last name", max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(help_text="Enter the user's location", max_length=256),
        ),
    ]