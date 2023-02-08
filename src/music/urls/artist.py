from rest_framework.routers import DefaultRouter

from music.views import ArtistViewSet

router = DefaultRouter()
router.register("artists", ArtistViewSet)

urlpatterns_artist = router.urls
