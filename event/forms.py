from django.forms import ModelForm, CharField
from event.models import Event
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse


class EventForm(ModelForm):

    description_full = CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 150},
        mce_attrs={
            'height': 600,
            'theme': "advanced",
        }
    ))

    class Meta:
        model = Event
