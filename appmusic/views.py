from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView
from appmusic.models import Library, Artist, Album, Track
from .forms import ArtistForm, AlbumForm, TrackForm, LibraryForm
from .serializers import LibrarySerializer, ArtistSerializer, AlbumSerializer, TrackSerializer
from django.utils.decorators import method_decorator
from django.utils import timezone

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'appmusic/form.html'

class LibraryList(ListView, ConnegResponseMixin):
    model = Library
    queryset = Library.objects.filter(date__lte=timezone.now()).order_by('date')[:5]
    context_object_name = 'latest_library_list'
    template_name = 'appmusic/library_list.html'

class LibraryDetail(DetailView, ConnegResponseMixin):
    model = Library
    template_name = 'appmusic/library_detail.html'

class LibraryCreate(LoginRequiredMixin, CreateView):
    model = Library
    template_name = 'appmusic/form.html'
    form_class = LibraryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LibraryCreate, self).form_valid(form)

class ArtistList(ListView, ConnegResponseMixin):
    model = Artist
    queryset = Artist.objects.filter()
    context_object_name = 'latest_artist_list'
    template_name = 'appmusic/artist_list.html'

class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    template_name = 'appmusic/form.html'
    form_class = ArtistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.library = Library.objects.get(id=self.kwargs['pk'])
        return super(ArtistCreate, self).form_valid(form)

class ArtistDetail(DetailView, ConnegResponseMixin):
    model = Artist
    template_name = 'appmusic/artist_detail.html'


class AlbumList(ListView, ConnegResponseMixin):
    model = Album
    queryset = Album.objects.filter()
    context_object_name = 'latest_album_list'
    template_name = 'appmusic/album_list.html'

class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    template_name = 'appmusic/form.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.library = Library.objects.get(id=self.kwargs['pk'])
        return super(AlbumCreate, self).form_valid(form)

class AlbumDetail(DetailView, ConnegResponseMixin):
    model = Album
    template_name = 'appmusic/album_detail.html'

class TrackList(ListView, ConnegResponseMixin):
    model = Track
    queryset = Track.objects.filter()
    context_object_name = 'latest_track_list'
    template_name = 'appmusic/track_list.html'

class TrackCreate(LoginRequiredMixin, CreateView):
    model = Track
    template_name = 'appmusic/form.html'
    form_class = TrackForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.library = Library.objects.get(id=self.kwargs['pk'])
        return super(TrackCreate, self).form_valid(form)

class TrackDetail(DetailView, ConnegResponseMixin):
    model = Track
    template_name = 'appmusic/track_detail.html'

@login_required()
### RESTful API views ###

class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APILibraryList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Library
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class APILibraryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Library
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class APIArtistList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class APIArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class APIAlbumList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class APIAlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class APITrackList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Track
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class APITrackDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Track
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
