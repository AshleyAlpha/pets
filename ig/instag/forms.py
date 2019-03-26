from .models import Profile,Image,Comment
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class PicForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile']

