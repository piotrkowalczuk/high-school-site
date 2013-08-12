from django.conf.urls import patterns
from information.views import NewsList


urlpatterns = patterns(
    '',
    (r'^news/', NewsList.as_view()),
)
