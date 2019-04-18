from .models import Pet, Client
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['user']

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

