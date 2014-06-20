from django.db import models


class GalleryManager(models.Manager):

    def get_all_published(self):
        return self.get_query_set().filter(is_published=True).order_by('-id')

    def get_published(self, id):
        return self.get_query_set().filter(id=id).filter(is_published=True)

class PhotoManager(models.Manager):

    def get_published_by_gallery(self, gallery_id):
        return self.get_query_set().filter(is_published=True).filter(gallery=gallery_id).order_by('id')
