from news.models import News, Category
from django.contrib import admin
from news.forms import NewsForm


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title',
        'autor',
        'category',
        'is_published',
        'is_pinned',
        'created_at',
        'updated_at',
        'slug'
    )

admin.site.register(News, NewsAdmin)
