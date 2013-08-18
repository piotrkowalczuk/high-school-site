from django.views.generic.base import View
from django.shortcuts import render
from models import News


class NewsList(View):
    def get(self, request):
        informations = News.objects.all()
        return render(
            request,
            'information/list.html',
            {'informations': informations}
        )


class NewsShow(View):
    def get(self, request, id):
        information = News.objects.get(pk=id)
        return render(
            request,
            'information/show.html',
            {'information': information}
        )
