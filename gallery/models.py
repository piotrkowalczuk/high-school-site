# -*- coding: utf-8 -*-
from django.db import models
from user.models import User
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os
import uuid


def image_filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '/'.join(['uploads/gallery', str(instance.gallery.id), filename])


def thumb_filepath(instance, filename):
    filename = 'thumb_'+filename
    return image_filepath(instance, filename)


class Gallery(models.Model):

    class Meta:
        verbose_name = "galeria"
        verbose_name_plural = "galerie"

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Photo(models.Model):

    class Meta:
        verbose_name = "zdjęcie"
        verbose_name_plural = "zdjęcia"

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_filepath)
    thumbnail = models.ImageField(
        upload_to=thumb_filepath,
        max_length=500,
        blank=True,
        null=True
    )
    autor = models.ForeignKey(User, related_name='Autor')
    gallery = models.ForeignKey(Gallery)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def image_preview(self):
        return u'<img src="/media/%s" />' % self.image

    image_preview.short_description = 'Podgląd zdjęcia'
    image_preview.allow_tags = True

    def create_thumbnail(self):

        if not self.image:
            return

        THUMBNAIL_SIZE = (100, 100)

        DJANGO_TYPE = self.image.file.content_type

        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        image = Image.open(StringIO(self.image.read()))

        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        suf = SimpleUploadedFile(
            os.path.split(self.image.name)[-1],
            temp_handle.read(),
            content_type=DJANGO_TYPE
        )

        self.thumbnail.save(
            '%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION),
            suf,
            save=False
        )

    def save(self):
        self.create_thumbnail()

        super(Photo, self).save()
