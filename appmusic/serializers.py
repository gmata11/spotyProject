from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Library, Artist, Album, Track

class LibrarySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='appmusic:library-detail')
    artists = HyperlinkedRelatedField(many=True, read_only=True, view_name='appmusic:library_detail')
    albums = HyperlinkedRelatedField(many=True, read_only=True, view_name='appmusic:album_detail')
    tracks = HyperlinkedRelatedField(many=True, read_only=True, view_name='appmusic:track_detail')
    user = CharField(read_only=True)

    class Meta:
        model = Library
        fields = ('uri','artists', 'albums', 'tracks', 'user')

class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='appmusic:artist-detail')
    Library = HyperlinkedRelatedField(view_name='appmusic:library_detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Artist
        fields = ('uri', 'nomArtista', 'tags', 'web', 'Library', 'user')


class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='appmusic:album-detail')
    library = HyperlinkedRelatedField(view_name='appmusic:library_detail', read_only=True)
    artist = HyperlinkedRelatedField(view_name='appmusic:artist_detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Album
        fields = ('uri', 'nomAlbum', 'releasedate', 'artist', 'library', 'user')


class TrackSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='appmusic:track-detail')
    library = HyperlinkedRelatedField(view_name='appmusic:library_detail', read_only=True)
    artist = HyperlinkedRelatedField(view_name='appmusic:artist_detail', read_only=True)
    album = HyperlinkedRelatedField(view_name='appmusic:album_detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Track
        fields = ('uri', 'nomTrack', 'duration', 'artist', 'album', 'library', 'user')
