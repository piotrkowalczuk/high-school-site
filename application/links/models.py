from django.db import models
from links.managers import LinkManager


class Link(models.Model):

    objects = LinkManager()

    class Meta:
        verbose_name = "link"
        verbose_name_plural = "linki"

    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    order = models.IntegerField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
