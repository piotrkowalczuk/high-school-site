from django.contrib import admin
from gallery.models import Gallery, Photo
from django.utils.safestring import mark_safe
from gallery.forms import PhotoInlineForm


class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('image_preview',)
    fields = (
        'name',
        'description',
        ('autor', 'gallery', 'slug'),
        'image',
        'image_preview'
    )

    def image_preview(self, obj):
        return mark_safe("""<img src="/media/%s" />""" % obj.image)


class PhotoInline(admin.TabularInline):
    model = Photo
    form = PhotoInlineForm


class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = (
        'name',
        'news',
        'description',
        'is_published'
    )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
