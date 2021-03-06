# Generated by Django 2.0.2 on 2018-04-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nintinder', '0017_auto_20180420_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, help_text="Enter the user's bio", max_length=1024),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(default='Player', help_text="Enter the user's title", max_length=64),
        ),
    ]
