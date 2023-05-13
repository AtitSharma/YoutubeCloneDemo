from django import forms
from video_player_app.models import User,Comment,Video
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]

class UserCommentForm(forms.ModelForm):
    description=forms.CharField(max_length=255,widget=forms.Textarea)
    class Meta:
        model=Comment
        fields=["description"]

class UserUploadVideoForm(forms.ModelForm):
    title=forms.CharField(max_length=255)
    description=forms.CharField(max_length=255,widget=forms.Textarea)
    video_file = forms.FileField()
    thumbnail=forms.ImageField()
    class Meta:
        model=Video
        fields=["title","description","video_file","thumbnail"]
