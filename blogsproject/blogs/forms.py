from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body',]

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search_word')

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'image',] 