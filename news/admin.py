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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'is_published',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
