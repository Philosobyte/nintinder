# Generated by Django 2.0.2 on 2018-03-16 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nintinder', '0007_auto_20180316_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='user_name',
        ),
    ]
