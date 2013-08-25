from django.forms import ModelForm, CharField
from news.models import News
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
