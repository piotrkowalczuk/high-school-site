from django.db import models
from user.models import User
from information.models import Information


def content_file_name(instance, filename):
    return '/'.join(['uploads', str(instance.gallery.id), filename])


class Gallery(models.Model):

    name = models.CharField(max_length=255)
    information = models.ForeignKey(Information, related_name='Information')
    description = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Photo(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    file = models.ImageField(upload_to=content_file_name)
    autor = models.ForeignKey(User, related_name='Autor')
    gallery = models.ForeignKey(Gallery, related_name='Gallery')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name
