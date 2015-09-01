from news.models import News
from django.contrib import admin
from news.forms import NewsForm


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title',
        'autor',
        'category',
        'semester',
        'event',
        'is_published',
        'is_pinned',
        'created_at',
        'updated_at',
        'slug'
    )
    list_filter = (
        ('is_pinned', admin.BooleanFieldListFilter),
        ('is_published', admin.BooleanFieldListFilter),
        'semester', 
        'category'
    )
    search_fields = ['title']

admin.site.register(News, NewsAdmin)
