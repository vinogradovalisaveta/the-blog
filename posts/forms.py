from django import forms
from posts.models import Post


class NewPostForm(forms.Form):
    model = Post
    fields = ['title', 'text']
