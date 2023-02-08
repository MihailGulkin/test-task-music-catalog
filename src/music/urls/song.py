from rest_framework.routers import DefaultRouter

from music.views import SongViewSet

router = DefaultRouter()
router.register("songs", SongViewSet)

urlpatterns_song = router.urls
