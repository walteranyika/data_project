from django.db import models


# Create your models here.
# https://medium.com/@soverignchriss/querying-related-objects-in-django-web-framework-3aece5bd927d
# https://docs.djangoproject.com/en/4.2/topics/db/queries/#additional-methods-to-handle-related-objects
# https://copyprogramming.com/howto/django-query-for-a-related-object

class Artist(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    artist = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    time = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title
