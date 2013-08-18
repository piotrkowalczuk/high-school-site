from news.models import News, Category
from django.contrib import admin


class NewsAdmin(admin.ModelAdmin):
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
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'name',
        'description',
        'is_published',
        'slug'
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
