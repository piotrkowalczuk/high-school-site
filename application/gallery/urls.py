from django.conf.urls import patterns, url
from gallery.views import GalleryIndex, GalleryShow


urlpatterns = patterns(
    '',
    url(r'^galleries', GalleryIndex.as_view(), name='gallery_index'),
    url(r'^gallery/(?P<id>\d+)/$', GalleryShow.as_view(), name='gallery_show'),
)
