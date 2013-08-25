from django.forms import ModelForm
from gallery.models import Photo
from gallery.widgets import AdminImageWidget


class PhotoInlineForm(ModelForm):
    class Meta:
        model = Photo
        fields = [
            'image',
            'description',
            'autor',
            'gallery',
        ]
        widgets = {'image': AdminImageWidget(), }
    readonly_fields = ('image_preview',)
