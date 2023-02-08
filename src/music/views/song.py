from rest_framework import viewsets

from music.serializers import SongSerializer
from music.models import Song


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
