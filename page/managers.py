from django.db import models


class PageManager(models.Manager):

    def get_published(self, slug):
        return self.get_query_set().filter(slug=slug).filter(is_published=True)

    def get_published_alphabetically(self, slug):
        return self.get_published(slug).order_by('-title')

    def all_alphabetically(self):
        return self.get_query_set().order_by('title')

    def all_published_alphabetically(self):
        return self.get_query_set().filter(is_published=True).order_by('title')
