from django.contrib.auth.models import User
from .models import Page, Diary
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ImageUrlForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['diary', 'title', 'tag', 'story']
