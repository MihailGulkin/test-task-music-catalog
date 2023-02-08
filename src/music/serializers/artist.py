from rest_framework import serializers

from music.models import Artist


class ArtisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'pk',
            'name'
        )
