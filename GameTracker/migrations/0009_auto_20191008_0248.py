# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-08 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameTracker', '0008_auto_20191001_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='in_library',
            field=models.BooleanField(default=True, verbose_name='Number of Participants'),
        ),
    ]
