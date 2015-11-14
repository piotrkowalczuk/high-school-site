from django.forms import Form, ModelForm, CharField, ModelChoiceField, Select
from tinymce.widgets import TinyMCE

from category.models import Category
from event.models import Event
from gallery.models import Gallery
from news.models import News
from semester.models import Semester


class NewsForm(ModelForm):
    content_body = CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 150},
        mce_attrs={
            'height': 600,
            'theme': "advanced",
        }
    ))

    class Meta:
        model = News

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['gallery'].queryset = Gallery.objects.order_by('-id')
        self.fields['event'].queryset = Event.objects.order_by('-id')
        self.fields['category'].queryset = Category.objects.order_by('id')
        self.fields['semester'].queryset = Semester.objects.order_by('-id')

class SearchForm(Form):
    semester = ModelChoiceField(queryset=Semester.objects.get_archived(),
                                widget=Select(attrs={'class': 'form-control', }))
    category = ModelChoiceField(queryset=Category.objects.get_sorted(),
                                widget=Select(attrs={'class': 'form-control', }))
