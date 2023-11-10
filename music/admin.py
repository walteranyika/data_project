from django.contrib import admin

from music.models import Album, Artist, Song


# Register your models here.
# https://www.geeksforgeeks.org/python-relational-fields-in-django-models/
# https://docs.djangoproject.com/en/4.2/topics/db/queries/#additional-methods-to-handle-related-objects

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone"]
    list_per_page = 25


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["name", "year"]
    list_per_page = 25


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["album", "title"]
    list_per_page = 25
