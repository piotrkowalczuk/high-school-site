# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name = "kategoria"
        verbose_name_plural = "kategorie"

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
