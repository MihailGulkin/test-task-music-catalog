from rest_framework import status
from rest_framework.test import (
    APITestCase,
    APIRequestFactory
)

from music.models import Artist
from music.serializers import ArtisSerializer
from music.views import ArtistViewSet

from music.tests.factory import make_artist


class ArtistTestCase(APITestCase):
    number_of_objects = 4

    api_req_factory = APIRequestFactory()

    request_get = api_req_factory.get('')
    request_delete = api_req_factory.delete('')

    request_create = api_req_factory.post('', {'name': 'test_create'})

    request_update = api_req_factory.patch('', {
        'name': 'test'
    })

    @classmethod
    def setUpTestData(cls):
        for index, artist in enumerate(make_artist(cls.number_of_objects)):
            setattr(
                cls,
                f'obj_{index}',
                artist
            )

    def test_get_all_artists(self):
        artist_detail = ArtistViewSet.as_view({'get': 'list'})

        response = artist_detail(self.request_get)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            ArtisSerializer(Artist.objects.all(), many=True).data
        )

    def test_get_artist(self):
        artist_detail = ArtistViewSet.as_view({'get': 'retrieve'})

        response = artist_detail(self.request_get, pk=self.obj_1.pk)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            ArtisSerializer(self.obj_1).data
        )

    def test_create_artist(self):
        artist_detail = ArtistViewSet.as_view({'post': 'create'})

        response = artist_detail(self.request_create)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertIn(
            response.data,
            ArtisSerializer(Artist.objects.all(), many=True).data
        )

    def test_delete_artist(self):
        artist_detail = ArtistViewSet.as_view({'delete': 'destroy'})

        response = artist_detail(self.request_delete, pk=self.obj_1.pk)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_patch_artist(self):
        pk = self.obj_2.pk

        artist_detail = ArtistViewSet.as_view({'patch': 'partial_update'})

        response = artist_detail(self.request_update, pk=pk)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertNotEqual(
            self.obj_2.name,
            Artist.objects.get(pk=pk).name
        )
