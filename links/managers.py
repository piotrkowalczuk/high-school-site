from django.db import models


class LinkManager(models.Manager):

    def get_published(self):
        return self.get_query_set().filter(is_published=True)
