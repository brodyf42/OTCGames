# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-29 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('player_count', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('in_library', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayedGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_player_count', models.PositiveSmallIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameTracker.Event')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameTracker.Game')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='games',
            field=models.ManyToManyField(through='GameTracker.PlayedGame', to='GameTracker.Game'),
        ),
    ]
