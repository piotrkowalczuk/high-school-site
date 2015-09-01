from models import Event
from forms import EventForm
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    form = EventForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title',
        'image',
        'autor',
        'is_published',
        'semester',
        'category',
        'start_at',
        'end_at',
    )
    list_filter = (
        ('is_published', admin.BooleanFieldListFilter),
        'semester', 
        'category'
    )
    search_fields = ['title']

admin.site.register(Event, EventAdmin)
