# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-01 02:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GameTracker', '0007_auto_20191001_0242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playedgame',
            options={'ordering': ['event']},
        ),
    ]
