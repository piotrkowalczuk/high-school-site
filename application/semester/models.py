# -*- coding: utf-8 -*-
from django.db import models
from semester.managers import SemesterManager


class Semester(models.Model):

    objects = SemesterManager()

    class Meta:
        verbose_name = "semestr"
        verbose_name_plural = "semestry"

    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
