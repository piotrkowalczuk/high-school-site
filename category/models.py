# -*- coding: utf-8 -*-
from django.db import models
from category.managers import CategoryManager


class Category(models.Model):

    objects = CategoryManager()

    class Meta:
        verbose_name = "kategoria"
        verbose_name_plural = "kategorie"

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        default=None,
        related_name="childrens"
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Nazwa'
    )
    description = models.TextField(verbose_name='Opis')
    is_published = models.BooleanField(
        default=False,
        verbose_name='Czy jest widoczna'
    )

    def __unicode__(self):
        return self.name

    def get_all_published(self):
        return self.page_set.filter(is_published=True)
