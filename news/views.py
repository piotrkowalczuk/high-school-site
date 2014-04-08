from common.views import BaseView
from django.shortcuts import render
from news.models import News
from event.models import Event
from links.models import Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class NewsIndex(BaseView):
    def get(self, request):
        news_not_pinned = News.objects.get_not_pinned()
        news_pinned = News.objects.get_pinned()[:3]
        events = Event.objects.get_published()[:5]
        links = Link.objects.get_published()
        paginator = Paginator(news_not_pinned, 1)

        try:
            news_list = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            news_list = paginator.page(1)
        except EmptyPage:
            news_list = paginator.page(paginator.num_pages)

        return render(
            request,
            'news/index.html',
            {
                'news_list': news_list,
                'news_pinned': news_pinned,
                'links': links,
                'menu': self.get_menu(),
                'events': events
            }
        )


class NewsList(BaseView):
    def get(self, request, category_name):
        news_not_pinned = News.objects.get_published_by_category(category_name=category_name)
        links = Link.objects.get_published()
        paginator = Paginator(news_not_pinned, 8)

        try:
            news_list = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            news_list = paginator.page(1)
        except EmptyPage:
            news_list = paginator.page(paginator.num_pages)

        return render(
            request,
            'news/list.html',
            {
                'news_list': news_list,
                'links': links,
                'menu': self.get_menu()
            }
        )


class NewsShow(BaseView):
    def get(self, request, slug):

        news = News.objects.get_published(slug=slug)
        links = Link.objects.get_published()

        return render(
            request,
            'news/show.html',
            {
                'news': news[0],
                'links': links,
                'menu': self.get_menu()
            }

        )
