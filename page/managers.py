from django.db import models


class PageManager(models.Manager):

    def get_published(self, slug):
        return self.get_query_set().filter(slug=slug).filter(is_published=True)
