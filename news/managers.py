from django.db import models


class NewsManager(models.Manager):

    def get_pinned(self):
        return self.get_query_set().filter(is_published=True).filter(is_pinned=True).order_by('-created_at', 'id')

    def get_not_pinned(self):
        return self.get_query_set().filter(is_published=True).filter(is_pinned=False).order_by('-created_at', 'id')

    def get_published_by_category(self, category_name):
        return self.get_query_set().filter(is_published=True).filter(category__name=category_name).order_by('-created_at', 'id')

    def get_published(self, slug):
        return self.get_query_set().filter(slug=slug).filter(is_published=True)
