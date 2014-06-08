from django.forms import ModelForm, CharField
from page.models import Page
from tinymce.widgets import TinyMCE


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
