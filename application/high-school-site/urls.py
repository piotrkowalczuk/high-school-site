from django.conf.urls import patterns, include, url
from django.conf import settings
from filebrowser.sites import site
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'', include('news.urls')),
    url(r'', include('page.urls')),
    url(r'', include('gallery.urls')),
    url(r'', include('event.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
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
