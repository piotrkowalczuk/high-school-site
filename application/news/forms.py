from django.forms import Form, ModelForm, CharField, ModelChoiceField, Select
from news.models import News
from semester.models import Semester
from category.models import Category
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse


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

class SearchForm(Form):
    semester = ModelChoiceField(queryset = Semester.objects.get_archived(), widget=Select(attrs={'class': 'form-control',}))
    category = ModelChoiceField(queryset = Category.objects.all(), widget=Select(attrs={'class': 'form-control',}))
