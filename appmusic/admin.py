from django.contrib import admin
from .models import Library, Artist, Album, Track, LibraryReview

admin.site.register(Library)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(LibraryReview)
