# -*- coding: utf-8 -*-
import uuid
from django.db import models
from user.models import User
from event.models import Event
from category.models import Category
from semester.models import Semester
from news.managers import NewsManager
from gallery.models import Gallery
from django.core.urlresolvers import reverse


def image_filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '/'.join(['uploads/news/thumbnail', filename])

def picture_filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '/'.join(['uploads/news/picture', filename])

class News(models.Model):

    objects = NewsManager()

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "newsy"

    title = models.CharField(
        max_length=255,
        verbose_name='Tytuł'
    )
    content_intro = models.TextField(verbose_name='Wprowadzenie wiadomości')
    content_body = models.TextField(verbose_name='Ciało wiadomości')
    autor = models.ForeignKey(
        User,
        verbose_name='Autor',
        related_name='News'
    )
    event = models.ForeignKey(
        Event,
        blank=True,
        null=True,
        verbose_name='Wydarzenie',
        related_name='news')
    is_published = models.BooleanField(
        default=False,
        verbose_name='Czy jest opublikowany'
    )
    is_pinned = models.BooleanField(
        default=False,
        verbose_name='Czy jest przypięty'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Kategoria'
    )
    semester = models.ForeignKey(
        Semester,
        verbose_name='Semestr'
    )
    gallery = models.ForeignKey(
        Gallery,
        blank=True,
        null=True,
        related_name='NewsGallery',
        verbose_name='Galeria'
    )
    image = models.ImageField(
        upload_to=image_filepath,
        null=True,
        blank=True,
        default=None,
        verbose_name='Miniaturka'
    )
    picture = models.ImageField(
        upload_to=picture_filepath,
        null=True,
        blank=True,
        default=None,
        verbose_name='Duży obrazek pod tekstem'
    )
    picture_description = models.TextField(
        verbose_name='Opis obrazka.',
        null=True,
        blank=True
    )
    slug = models.SlugField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_show', args=[str(self.slug)])
