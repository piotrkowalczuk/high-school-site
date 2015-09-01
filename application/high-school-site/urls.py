from django.conf.urls import patterns, include, url
from django.conf import settings
from filebrowser.sites import site
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from news.sitemap import NewsSitemap
from page.sitemap import PageSitemap
from gallery.sitemap import GallerySitemap, PhotoSitemap
from event.sitemap import EventSitemap

admin.autodiscover()

sitemaps = {
    'news': NewsSitemap,
    'page': PageSitemap,
    'gallery': GallerySitemap,
    'photo': PhotoSitemap,
    'event': EventSitemap,
}

urlpatterns = patterns(
    '',
    url(r'', include('news.urls')),
    url(r'', include('page.urls')),
    url(r'', include('gallery.urls')),
    url(r'', include('event.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/',  include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        )
    )
