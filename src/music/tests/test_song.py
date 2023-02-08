from rest_framework import status
from rest_framework.test import (
    APITestCase,
    APIRequestFactory
)

from music.models import Song
from music.serializers import SongSerializer
from music.views import SongViewSet

from music.tests.factory import (
    make_song,
    make_album
)


class SongTestCase(APITestCase):
    number_of_objects = 4

    api_req_factory = APIRequestFactory()

    request_get = api_req_factory.get('')
    request_delete = api_req_factory.delete('')

    @classmethod
    def setUpTestData(cls):
        for index, song in enumerate(make_song(cls.number_of_objects)):
            setattr(
                cls,
                f'obj_{index}',
                song
            )

    def test_get_all_songs(self):
        song_detail = SongViewSet.as_view({'get': 'list'})

        response = song_detail(self.request_get)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            SongSerializer(Song.objects.all(), many=True).data
        )

    def test_get_song(self):
        song_detail = SongViewSet.as_view({'get': 'retrieve'})

        response = song_detail(self.request_get, pk=self.obj_1.pk)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            SongSerializer(self.obj_1).data
        )

    def test_create_song(self):
        albums = make_album(3)

        request_create = self.api_req_factory.post('', {
            'title': 'some_Name',
            'albums_id': [
                album.pk
                for album in albums
            ]

        })
        song_detail = SongViewSet.as_view({'post': 'create'})

        response = song_detail(request_create)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertIn(
            response.data,
            SongSerializer(Song.objects.all(), many=True).data
        )

    def test_delete_song(self):
        song_detail = SongViewSet.as_view({'delete': 'destroy'})

        response = song_detail(self.request_delete, pk=self.obj_1.pk)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_patch_song(self):
        request_update = self.api_req_factory.patch('', {
            'title': 'test'
        })

        pk = self.obj_2.pk

        song_detail = SongViewSet.as_view({'patch': 'partial_update'})

        response = song_detail(request_update, pk=pk)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertNotEqual(
            self.obj_2.title,
            Song.objects.get(pk=pk).title
        )
