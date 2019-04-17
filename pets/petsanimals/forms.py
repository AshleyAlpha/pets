from .models import Pet, Client
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['user']

