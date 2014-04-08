# -*- coding: utf-8 -*-
from django.db import models
from user.models import User
from category.models import Category
from semester.models import Semester
from event.managers import EventManager
from gallery.models import Gallery
import uuid
import image.thumbnails as thumbnails
from cStringIO import StringIO
from PIL import Image


class Event(models.Model):

    objects = EventManager()

    class Meta:
        verbose_name = "wydarzenie"
        verbose_name_plural = "wydarzenia"

    title = models.CharField(
        max_length=255,
        verbose_name='Tytuł'
    )
    description_short = models.TextField(verbose_name='Skrócony opis wydarzenia')
    description_full = models.TextField(verbose_name='Pełny opis wydarzenia')
    autor = models.ForeignKey(
        User,
        verbose_name='Autor',
        related_name='Event'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Czy jest opublikowany'
    )
    semester = models.ForeignKey(
        Semester,
        verbose_name='Semestr'
    )
    slug = models.SlugField(unique=True, max_length=100)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
