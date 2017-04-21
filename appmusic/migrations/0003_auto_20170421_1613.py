# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmusic', '0002_auto_20170417_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='user',
        ),
        migrations.RemoveField(
            model_name='libraryreview',
            name='library',
        ),
        migrations.RemoveField(
            model_name='libraryreview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='album',
            name='Library',
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='album',
            name='releasedate',
        ),
        migrations.RemoveField(
            model_name='album',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
        migrations.RemoveField(
            model_name='album',
            name='web',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='Library',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='similars',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='web',
        ),
        migrations.RemoveField(
            model_name='track',
            name='Library',
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.RemoveField(
            model_name='track',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='track',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='track',
            name='playcount',
        ),
        migrations.RemoveField(
            model_name='track',
            name='published',
        ),
        migrations.RemoveField(
            model_name='track',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='track',
            name='user',
        ),
        migrations.RemoveField(
            model_name='track',
            name='web',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.DeleteModel(
            name='LibraryReview',
        ),
    ]