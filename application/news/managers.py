from django.db import models


class NewsManager(models.Manager):

    def get_pinned_in_semester(self):
        return self.get_query_set().filter(is_published=True, semester__is_active=True, is_pinned=True).order_by('-created_at', 'id')

    def get_not_pinned_in_semester(self):
        return self.get_query_set().filter(is_published=True, semester__is_active=True, is_pinned=False).order_by('-created_at', 'id')

    def get_published_by_category(self, category_name):
        return self.get_query_set().filter(is_published=True, category__name=category_name).order_by('-created_at', 'id')

    def get_published_in_active_semester_by_category(self, category_name):
        return self.get_query_set().filter(is_published=True, semester__is_active=True, category__name=category_name).order_by('-created_at', 'id')

    def get_archived_by_category_and_semester(self, category_id, semester_id):
        kwargs = {
            'is_published': True,
            '{0}__{1}'.format('semester', 'is_active'): False
        }

        if(isinstance(category_id, ( int, long )) and category_id > 0):
            kwargs['category_id'] = category_id

        if(isinstance(semester_id, ( int, long )) and semester_id > 0):
            kwargs['semester_id'] = semester_id

        return self.get_query_set().filter(**kwargs).order_by('-created_at', 'id')

    def get_published(self, slug):
        return self.get_query_set().filter(slug=slug, is_published=True)
