from django.conf.urls import patterns, url
from news.views import NewsIndex, NewsList, NewsShow, NewsArchive


urlpatterns = patterns(
    '',
    url(r'^$', NewsIndex.as_view(), name='news_list'),
    url(r'^news/(?P<slug>[\w-]+)/$', NewsShow.as_view(), name='news_show'),
    url(
        r'^news/filter/(?P<category_name>[\w-]+)/$',
        NewsList.as_view(),
        name='news_filter'
    ),
    url(
        r'^news-archiwum/$',
        NewsArchive.as_view(),
        name='news_archive'
    ),
)
