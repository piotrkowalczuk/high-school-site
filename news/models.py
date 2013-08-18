# -*- coding: utf-8 -*-
from django.db import models
from user.models import User
from category.models import Category
from semester.models import Semester


class Category(Category):
    pass


class News(models.Model):

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
        related_name='Information'
    )
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
    slug = models.SlugField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
