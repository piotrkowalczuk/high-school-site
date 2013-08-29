from django.contrib import admin
from menu.models import Menu, MenuElement


class MenuAdmin(admin.ModelAdmin):

    fields = (
        'name',
        'url',
        'order',
        'is_published'
    )

    list_display = (
        'name',
        'url',
        'order',
        'is_published',
        'created_at',
        'updated_at'
    )


class MenuElementAdmin(admin.ModelAdmin):

    fields = (
        'name',
        'url',
        'order',
        'menu',
        'is_published'
    )

    list_display = (
        'name',
        'url',
        'order',
        'menu',
        'is_published',
        'created_at',
        'updated_at'
    )

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuElement, MenuElementAdmin)
