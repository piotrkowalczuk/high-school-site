from common.views import BaseView
from django.shortcuts import render
from page.models import Page


class PageShow(BaseView):
    def get(self, request, slug):

        page = Page.objects.get_published(slug=slug)

        return render(
            request,
            'page/show.html',
            {
                'page': page[0],
                'menu': self.get_menu()
            }

        )
