from .models import Profile,Image,Comment,Like
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class PicForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile']

class CommentForm(forms.Form):
        comment =forms.CharField(label='Comment',max_length = 300)
        
class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ['user']        

