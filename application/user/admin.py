from django.contrib import admin
from user.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.register(User)
admin.site.unregister(Site)
admin.site.unregister(Group)
