from django import forms
from .models import Photo, Blog

class PostForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            "file",
        ]
        # widgets = {'description': forms.TextInput(
        #         attrs={'placeholder': '(Optional)'})}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "category",
            "tags",
            "img_url"
        ]
        widgets = {'img_url': forms.HiddenInput()}