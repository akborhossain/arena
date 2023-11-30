from django import forms
from django.contrib.auth.models import User
from .models import Event
from django.utils import timezone
import datetime

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'event_time']

    event_time = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(datetime.date.today().year, datetime.date.today().year + 10),
            months={'': '--', **{str(i): i for i in range(1, 13)}},
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
            attrs={'class': 'form-control'}  # Add 'form-control' class to the widget
        ),
        initial=datetime.date.today()
    )

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
