# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 22:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmusic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='ibrary',
            new_name='Library',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='nameArtist',
            new_name='nomArtista',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='genere',
            new_name='summary',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='resum',
            new_name='tags',
        ),
    ]
