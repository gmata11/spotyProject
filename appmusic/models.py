from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date



class Artist(models.Model):
    nomArtista = models.TextField()
    tags = models.TextField(blank=True)
    web = models.URLField(blank=True)




class Album(models.Model):
    nomAlbum = models.TextField()
    releasedate = models.TextField(blank=True)
    artist = models.ForeignKey(Artist, blank=True, null=True)


class Track(models.Model):
    nomTrack = models.TextField()
    duration = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(Artist, blank=True, null=True)
    album = models.ForeignKey(Album, blank=True, null=True)
