# Generated by Django 4.1.6 on 2023-02-11 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indigoshoot', '0003_rename_host_round_team_host_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='DAY1_POINTS',
        ),
        migrations.RemoveField(
            model_name='score',
            name='DAY2_POINTS',
        ),
        migrations.RemoveField(
            model_name='score',
            name='DAY3_POINTS',
        ),
        migrations.RemoveField(
            model_name='score',
            name='DAY4_POINTS',
        ),
        migrations.RemoveField(
            model_name='score',
            name='DAY5_POINTS',
        ),
    ]
