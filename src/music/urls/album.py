from rest_framework.routers import DefaultRouter

from music.views import AlbumViewSet

router = DefaultRouter()
router.register("albums", AlbumViewSet)

urlpatterns_album = router.urls
