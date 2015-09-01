# -*- coding: utf-8 -*-
from django.db import models
from user.models import User
from category.models import Category
from semester.models import Semester
from event.managers import EventManager
import uuid
from django.utils import timezone
from django.core.urlresolvers import reverse


def image_filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '/'.join(['uploads/calendar/thumbnails', filename])

class Event(models.Model):
    STATUS_ANY = 0
    STATUS_INCOMING = 1
    STATUS_IN_PROGRESS = 2
    STATUS_FINISHED = 3

    objects = EventManager()

    class Meta:
        verbose_name = "wydarzenie"
        verbose_name_plural = "wydarzenia"

    title = models.CharField(
        max_length=255,
        verbose_name='Tytuł'
    )
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    category = models.ForeignKey(
        Category,
        verbose_name='Kategoria'
    )
    autor = models.ForeignKey(
        User,
    )
    description = models.TextField(verbose_name='Opis')
    is_published = models.BooleanField(
        default=False,
        verbose_name='Czy jest opublikowany'
    )
    semester = models.ForeignKey(
        Semester,
        verbose_name='Semestr',
    )
    image = models.ImageField(
        upload_to=image_filepath,
        null=True,
        blank=True,
        default=None,
        verbose_name='Miniaturka'
    )
    slug = models.SlugField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_details', args=[str(self.slug)])

    @property 
    def status(self):
        now = timezone.localtime(timezone.now())

        try:
            if now >= self.start_at and now <= self.end_at:
                return self.STATUS_IN_PROGRESS
            if now > self.end_at:
                return self.STATUS_FINISHED
            if now < self.start_at:
                return self.STATUS_INCOMING

            return self.STATUS_ANY
        except TypeError:
            print "datetime comparison TypeError"


EVENT_STATUS_CHOICES = (
    (Event.STATUS_ANY, 'Najbliższe'),
    (Event.STATUS_INCOMING, 'Nadchodzące'),
    (Event.STATUS_IN_PROGRESS, 'W trakcie'),
    (Event.STATUS_FINISHED, 'Zakończone'),
)