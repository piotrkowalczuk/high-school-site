from django.forms import ModelForm
from gallery.models import Photo
from gallery.widgets import AdminImageWidget
from django.forms import Form, ModelForm, CharField, ModelChoiceField, Select
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

class SearchForm(Form):
    semester = ModelChoiceField(queryset = Semester.objects.get_archived(), widget=Select(attrs={'class': 'form-control',}))
