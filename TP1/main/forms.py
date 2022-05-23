from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
#        fields = ('author','description')
        fields = ["author","description"]

    widgets = {
        "author": forms.Select(attrs={'class':'form-control', 'value':'', 'type':'hidden','hidden':True})
    }
