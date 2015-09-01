from django.forms import Form, ModelForm, CharField, ModelChoiceField, Select, ChoiceField
from event.models import Event, EVENT_STATUS_CHOICES
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse
from semester.models import Semester
from category.models import Category


class EventForm(ModelForm):
    class Meta:
        model = Event
        prepopulated_fields = {"autor": (1,)}

class FilterForm(Form):
    semester = ModelChoiceField(queryset = Semester.objects.all(), widget=Select(attrs={'class': 'form-control',}))
    category = ModelChoiceField(queryset = Category.objects.all(), widget=Select(attrs={'class': 'form-control',}))
    status = ChoiceField(choices=EVENT_STATUS_CHOICES)
