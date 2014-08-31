from django.conf.urls import patterns, url
from gallery.views import GalleryIndex, GalleryShow, GalleryArchive


urlpatterns = patterns(
    '',
    url(
        r'^galerie-archiwum/$',
        GalleryArchive.as_view(),
        name='gallery_archive'
    ),
    url(r'^galerie', GalleryIndex.as_view(), name='gallery_index'),
    url(r'^galeria/(?P<id>\d+)/$', GalleryShow.as_view(), name='gallery_show'),
)
