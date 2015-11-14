from django.forms import ModelForm, CharField
from tinymce.widgets import TinyMCE

from category.models import Category
from gallery.models import Gallery
from page.models import Page


class PageForm(ModelForm):
    content = CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 150},
        mce_attrs={
            'height': 600,
            'theme': "advanced",
        }
    ))

    class Meta:
        model = Page

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.fields['gallery'].queryset = Gallery.objects.order_by('-id')
        self.fields['category'].queryset = Category.objects.order_by('id')
