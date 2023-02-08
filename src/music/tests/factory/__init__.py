from .base_factory import create_model_factory

make_song = create_model_factory('music.Song')
make_artist = create_model_factory('music.Artist')
make_album = create_model_factory('music.Album')
