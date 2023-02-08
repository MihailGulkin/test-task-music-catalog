from rest_framework import viewsets

from music.serializers import AlbumSerializer
from music.models import Album


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
