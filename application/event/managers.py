from django.db import models
from django.utils import timezone
from datetime import timedelta
import calendar

class EventManager(models.Manager):

    def get_published(self, slug):
        return self.get_query_set().filter(is_published=True)

    def get_published(self, start, end):
        return self.get_query_set().filter(is_published=True, start_at__gt=start, end_at__lt=end).order_by('id')

    def get_by_slug(self, slug): 
        return self.get_query_set().filter(
            is_published=True,
            slug__exact=slug,
        )[:1].get()

    def get_for_current_month(self):
        now = timezone.localtime(timezone.now())
        day1, day2 = calendar.monthrange(now.year, now.month)

        start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        end = now.replace(day=day2, hour=23, minute=59, second=59, microsecond=9999)

        return self.get_query_set().filter(start_at__lte=end, end_at__gte=start).order_by('end_at', '-start_at',  'id')

    def get_ongoing(self):
        now = timezone.localtime(timezone.now())

        return self.get_query_set().filter(start_at__lt=now, end_at__gt=now).order_by('start_at', 'end_at', 'id')

    def get_starting_in_next_days(self, days):
        now = timezone.localtime(timezone.now())
        end = now + timedelta(days=days)

        return self.get_query_set().filter(start_at__gt=now, start_at__lt=end).order_by('start_at', 'end_at', 'id')

    def get_for_next_days(self, days):
        now = timezone.localtime(timezone.now())
        end = now + timedelta(days=days)

        return self.get_query_set().filter(end_at__gt=now, end_at__lt=end).order_by('end_at', '-start_at',  'id')

    def get_filtered(self, semester_id, category_id, status):
        now = timezone.localtime(timezone.now())

        kwargs = {
            'is_published': True,
        }

        if(isinstance(category_id, ( int, long )) and category_id > 0):
            kwargs['category_id'] = category_id

        if(isinstance(semester_id, ( int, long )) and semester_id > 0):
            kwargs['semester_id'] = semester_id

        if status == 3:
            kwargs['end_at__lt'] = now
        elif status == 2:
            kwargs['end_at__gte'] = now
            kwargs['start_at__lte'] = now
        elif status == 1:
            kwargs['start_at__gt'] = now
        elif status == 0:
            kwargs['start_at__lte'] = now

        return self.get_query_set().filter(**kwargs).order_by('-start_at', '-end_at', 'id')