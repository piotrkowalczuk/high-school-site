from category.models import Category
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'is_published',
    )

admin.site.register(Category, CategoryAdmin)
