from django.db import models


class GalleryManager(models.Manager):

    def get_all_published(self):
        return self.get_query_set().filter(is_published=True).order_by('-id')

    def get_published(self, id):
        return self.get_query_set().filter(id=id).filter(is_published=True)

    def get_published_for_active_semester(self):
        return self.get_query_set().filter(is_published=True).filter(semester__is_active=True).order_by('-id')

    def get_archived_by_semester(self, semester_id):
        query = self.get_query_set().filter(is_published=True).filter(semester__is_active=False)

        if(isinstance(semester_id, ( int, long ))):
            query = query.filter(semester_id=semester_id)

        return query.order_by('-id')


class PhotoManager(models.Manager):

    def get_published_by_gallery(self, gallery_id):
        return self.get_query_set().filter(is_published=True).filter(gallery=gallery_id).order_by('id')
