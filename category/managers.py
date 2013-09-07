from django.db import models


class CategoryManager(models.Manager):

    def get_mains(self):
        return self.get_query_set().filter(parent__isnull=True)
