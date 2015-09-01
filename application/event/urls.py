from django.conf.urls import patterns, url
from event.views import EventList, EventDetails

urlpatterns = patterns(
    '',
    url(r'^wydarzenia/', EventList.as_view(), name='event_list'),
    url(r'^wydarzenie/(?P<slug>[\w-]+)/$', EventDetails.as_view(), name='event_details'),
)
