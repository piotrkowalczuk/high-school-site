from common.views import BaseView
from django.shortcuts import render
from news.models import News
from event.models import Event
from gallery.models import Photo
from links.models import Link
from news.forms import SearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class NewsIndex(BaseView):
    def get(self, request):
        news_not_pinned = News.objects.get_not_pinned_in_semester()
        news_pinned = News.objects.get_pinned_in_semester()[:3]
        links = Link.objects.get_published()
        paginator = Paginator(news_not_pinned, 10)

        try:
            news_list = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            news_list = paginator.page(1)
        except EmptyPage:
            news_list = paginator.page(paginator.num_pages)

        events = Event.objects.get_for_current_month()

        return render(
            request,
            'news/index.html',
            {
                'news_list': news_list,
                'news_pinned': news_pinned,
                'links': links,
                'menu': self.get_menu(),
                'events': events,
            }
        )


class NewsList(BaseView):
    def get(self, request, category_name):
        news_not_pinned = News.objects.get_published_in_active_semester_by_category(category_name=category_name)
        links = Link.objects.get_published()
        paginator = Paginator(news_not_pinned, 10)

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
                'category_name': category_name,
                'news_list': news_list,
                'links': links,
                'menu': self.get_menu()
            }
        )


class NewsShow(BaseView):
    def get(self, request, slug):

        news = News.objects.get_published(slug=slug)[0]
        links = Link.objects.get_published()
        photos = Photo.objects.get_published_by_gallery(gallery_id=news.gallery_id)

        return render(
            request,
            'news/show.html',
            {
                'news': news,
                'links': links,
                'menu': self.get_menu(),
                'photos': photos
            }

        )

class NewsArchive(BaseView):
    def get(self, request):
        form = SearchForm(request.GET)
        semester_id = int('0' + request.GET.get('semester', '0'))
        category_id = int('0' + request.GET.get('category', '0'))

        archives = News.objects.get_archived_by_category_and_semester(category_id=category_id, semester_id=semester_id)
        paginator = Paginator(archives, 10)

        try:
            archives_list = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            archives_list = paginator.page(1)
        except EmptyPage:
            archives_list = paginator.page(paginator.num_pages)

        return render(
            request,
            'news/archive.html',
            {
                'archives_list': archives_list,
                'menu': self.get_menu(),
                'form': form,
                'semester_id': semester_id,
                'category_id': category_id
            }
        )
