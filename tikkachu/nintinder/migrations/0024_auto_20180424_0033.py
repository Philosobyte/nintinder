# Generated by Django 2.0.2 on 2018-04-24 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nintinder', '0023_auto_20180424_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'friends'), (1, 'pending'), (1, 'blacklist')]),
        ),
    ]
