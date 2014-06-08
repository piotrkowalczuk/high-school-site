from django.db import models


class NewsManager(models.Manager):

    def get_pinned(self):
        return self.get_query_set().filter(is_published=True).filter(is_pinned=True).order_by('-created_at', 'id')

    def get_not_pinned(self):
        return self.get_query_set().filter(is_published=True).filter(is_pinned=False).order_by('-created_at', 'id')

    def get_published_by_category(self, category_name):
        return self.get_query_set().filter(is_published=True).filter(category__name=category_name).order_by('-created_at', 'id')

    def get_archived_by_category_and_semester(self, category_id, semester_id):
        query = self.get_query_set().filter(is_published=True).filter(semester__is_active=False)

        if(category_id):
            print category_id
            query = query.filter(category_id=category_id)

        if(semester_id):
            query = query.filter(semester_id=semester_id)

        return query.order_by('-created_at', 'id')

    def get_published(self, slug):
        return self.get_query_set().filter(slug=slug).filter(is_published=True)
