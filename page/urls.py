from django.conf.urls import patterns, url
from page.views import PageShow


urlpatterns = patterns(
    '',
    url(r'^page/(?P<slug>[\w-]+)/$', PageShow.as_view(), name='page_show'),
)
