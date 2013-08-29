from page.models import Page, Category
from django.contrib import admin
from page.forms import PageForm


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title',
        'autor',
        'category',
        'is_published',
        'created_at',
        'updated_at',
        'slug'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'is_published'
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
