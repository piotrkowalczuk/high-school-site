from django.forms import Form, ModelForm, ModelChoiceField, Select

from gallery.models import Photo, Gallery
from gallery.widgets import AdminImageWidget
from semester.models import Semester


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

    def __init__(self, *args, **kwargs):
        super(PhotoInlineForm, self).__init__(*args, **kwargs)

        self.fields['gallery'].queryset = Gallery.objects.order_by('-id')


class SearchForm(Form):
    semester = ModelChoiceField(queryset=Semester.objects.get_archived(),
                                widget=Select(attrs={'class': 'form-control', }))
