from page.models import Page
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
    list_filter = (
        ('is_published', admin.BooleanFieldListFilter),
        'category'
    )
    search_fields = ['title']

admin.site.register(Page, PageAdmin)
