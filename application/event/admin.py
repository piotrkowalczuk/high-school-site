from event.models import Event
from event.forms import EventForm
from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    form = EventForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title',
        'autor',
        'description_short',
        'is_published',
        'created_at',
        'updated_at',
        'slug'
    )

admin.site.register(Event, EventAdmin)
