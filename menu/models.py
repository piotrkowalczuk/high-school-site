# -*- coding: utf-8 -*-
from django.db import models
from menu.managers import MenuManager


class Menu(models.Model):

    objects = MenuManager()

    class Meta:
        verbose_name = "menu"
        verbose_name_plural = "menu"

    name = models.CharField(max_length=255)
    url = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    order = models.IntegerField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class MenuElement(models.Model):

    objects = MenuManager()

    class Meta:
        verbose_name = "menu"
        verbose_name_plural = "menu"

    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    order = models.IntegerField()
    is_published = models.BooleanField(default=False)
    menu = models.ForeignKey(
        Menu,
        verbose_name='Menu',
        related_name='MenuElement'
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
