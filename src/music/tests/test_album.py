import datetime

from rest_framework import status
from rest_framework.test import (
    APITestCase,
    APIRequestFactory
)

from music.models import Album
from music.serializers import AlbumSerializer
from music.views import AlbumViewSet

from music.tests.factory import (
    make_artist,
    make_album
)


class AlbumTestCase(APITestCase):
    number_of_objects = 4

    api_req_factory = APIRequestFactory()

    request_get = api_req_factory.get('')
    request_delete = api_req_factory.delete('')

    @classmethod
    def setUpTestData(cls):
        for index, album in enumerate(make_album(cls.number_of_objects)):
            setattr(
                cls,
                f'obj_{index}',
                album
            )

    def test_get_all_albums(self):
        album_detail = AlbumViewSet.as_view({'get': 'list'})

        response = album_detail(self.request_get)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            AlbumSerializer(Album.objects.all(), many=True).data
        )

    def test_get_album(self):
        album_detail = AlbumViewSet.as_view({'get': 'retrieve'})

        response = album_detail(self.request_get, pk=self.obj_1.pk)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            AlbumSerializer(self.obj_1).data
        )

    def test_create_album(self):
        artist = make_artist()

        request_create = self.api_req_factory.post('', {
            'artist': artist.pk,
            'release_year': datetime.date.today()

        })
        album_detail = AlbumViewSet.as_view({'post': 'create'})

        response = album_detail(request_create)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertIn(
            response.data,
            AlbumSerializer(Album.objects.all(), many=True).data
        )

    def test_delete_album(self):
        album_detail = AlbumViewSet.as_view({'delete': 'destroy'})

        response = album_detail(self.request_delete, pk=self.obj_1.pk)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_patch_album(self):
        artist = make_artist()
        request_update = self.api_req_factory.patch('', {
            'artist': artist.pk
        })

        pk = self.obj_2.pk

        album_detail = AlbumViewSet.as_view({'patch': 'partial_update'})

        response = album_detail(request_update, pk=pk)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertNotEqual(
            self.obj_2.artist.pk,
            artist.pk
        )
