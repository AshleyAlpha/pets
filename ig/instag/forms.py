from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']