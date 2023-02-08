from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE
    )
    release_year = models.DateField()


class Song(models.Model):
    name = models.CharField(max_length=100)
    album_id = models.ManyToManyField(
        Album,
        blank=True
    )
