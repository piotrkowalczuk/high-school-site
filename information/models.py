from django.db import models
from user.models import User


class InformationCategory(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Information(models.Model):

    title = models.TextField()
    content = models.TextField()
    autor = models.ForeignKey(User, related_name='Information')
    is_published = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    category = models.ForeignKey(InformationCategory)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
