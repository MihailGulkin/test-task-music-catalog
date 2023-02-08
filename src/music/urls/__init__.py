from django.urls import (
    path,
    include
)

from .artist import urlpatterns_artist
from .album import urlpatterns_album
from .song import urlpatterns_song

urlpatterns = [
    path('music/', include(urlpatterns_artist)),
    path('album/', include(urlpatterns_album)),
    path('song/', include(urlpatterns_song))
]
