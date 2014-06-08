from django.db import models


class SemesterManager(models.Manager):

    def get_archived(self):
        return self.get_query_set().filter(is_active=False)
