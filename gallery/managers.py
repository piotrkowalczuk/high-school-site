from django.db import models


class GalleryManager(models.Manager):

    def get_all_published(self):
        return self.get_query_set().filter(is_published=True)

    def get_published(self, id):
        return self.get_query_set().filter(id=id).filter(is_published=True)