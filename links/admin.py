from django.contrib import admin
from links.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
        'order'
    )

admin.site.register(Link, LinkAdmin)
