# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmusic', '0009_libraryreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='summary',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
