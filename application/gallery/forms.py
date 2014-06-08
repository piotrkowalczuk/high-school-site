from django.forms import ModelForm
from gallery.models import Photo
from gallery.widgets import AdminImageWidget


class PhotoInlineForm(ModelForm):
    class Meta:
        model = Photo
        prepopulated_fields = {"autor": (1,)}
        fields = [
            'image',
            'description',
            'is_published',
            'autor',
            'gallery',
        ]
        widgets = {'image': AdminImageWidget(), }
    readonly_fields = ('image_preview',)
