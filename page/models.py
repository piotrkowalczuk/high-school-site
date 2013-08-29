# -*- coding: utf-8 -*-
from django.db import models
from user.models import User
from category.models import Category
from semester.models import Semester
from page.managers import PageManager
from gallery.models import Gallery


class Category(Category):
    pass


class Page(models.Model):

    objects = PageManager()

    class Meta:
        verbose_name = "strona"
        verbose_name_plural = "strony"

    title = models.CharField(
        max_length=255,
        verbose_name='Tytuł'
    )
    content = models.TextField(verbose_name='Treść')
    autor = models.ForeignKey(
        User,
        verbose_name='Autor',
        related_name='Page'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Czy jest opublikowany'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Kategoria'
    )
    gallery = models.ForeignKey(
        Gallery,
        blank=True,
        null=True,
        related_name='PageGallery'
    )
    slug = models.SlugField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
