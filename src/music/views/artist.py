from rest_framework import viewsets

from music.serializers import ArtisSerializer
from music.models import Artist


class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtisSerializer
    queryset = Artist.objects.all()
    