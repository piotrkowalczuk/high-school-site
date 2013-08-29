from django.views.generic.base import View
from page.models import Category


class BaseView(View):
    def get_menu(self):
        menu = Category.objects.all()

        return menu
