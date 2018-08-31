from django import forms
from .models import Photo, Blog, Provider

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
            "img_url",
            "provider"
        ]
        widgets = {'img_url': forms.HiddenInput()}

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [
            "provider_name",
            "description",
            "url",
            "favicon_url",
        ]
        # widgets = {'url': forms.TextInput(
        #         attrs={'placeholder': '(Optional)'})}