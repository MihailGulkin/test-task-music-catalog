from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Album(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE
    )
    release_year = models.DateField()

    def __str__(self):
        return f'{self.pk} - {self.artist.name}'


class Song(models.Model):
    title = models.CharField(max_length=100)
    albums_id = models.ManyToManyField(
        Album,
        blank=True
    )

    def __str__(self):
        return f'{self.pk} - {self.title}'
