from django.db import models


class MenuManager(models.Manager):

    def get_published(self):
        return self.get_query_set().filter(is_published=True)
