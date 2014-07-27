from common.views import BaseView
from django.shortcuts import render
from page.models import Page


class PageShow(BaseView):
    def get(self, request, slug):

        pages = Page.objects.get_published(slug=slug)
        page = pages[0]

        if str(page.updated_at) == '1970-01-01 00:00:00':
            page.updated_at = page.created_at

        return render(
            request,
            'page/show.html',
            {
                'page': page,
                'menu': self.get_menu()
            }

        )
