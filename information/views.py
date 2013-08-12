from django.views.generic.base import View
from django.shortcuts import render

from models import Information


class NewsList(View):
    def get(self, request):
        informations = Information.objects.all()
        return render(
            request,
            'information/list.html',
            {'informations': informations}
        )
