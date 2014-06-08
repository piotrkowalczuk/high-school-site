from django.db import models
import datetime

class EventManager(models.Manager):

    def get_published(self, slug):
        return self.get_query_set().filter(slug=slug).filter(is_published=True)

    def get_published(self):
        return self.get_query_set().filter(is_published=True, end_at__gt=datetime.datetime.now()).order_by('-end_at')
