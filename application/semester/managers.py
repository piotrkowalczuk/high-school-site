from django.db import models


class SemesterManager(models.Manager):

    def get_archived(self):
        return self.get_query_set().filter(is_active=False).order_by('-name', 'id')

    def get_sorted(self):
        return self.get_query_set().order_by('-name', 'id')

