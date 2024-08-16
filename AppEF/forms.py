from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from ckeditor.widgets import CKEditorWidget

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)


class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'subheader', 'body', 'image']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)