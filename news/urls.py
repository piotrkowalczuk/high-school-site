from django.conf.urls import patterns, url
from news.views import NewsList, NewsShow


urlpatterns = patterns(
    '',
    url(r'^$', NewsList.as_view(), name='news_list'),
    url(r'^news/(?P<slug>[\w-]+)/$', NewsShow.as_view(), name='news_show'),
)
