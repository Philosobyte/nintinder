# Generated by Django 2.0.2 on 2018-04-24 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nintinder', '0021_auto_20180423_1222'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together={('friendA', 'friendB')},
        ),
    ]
