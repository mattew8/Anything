from django import forms
from .models import Comment, Post, ReComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]

class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ['body',]

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search_word')

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'image',] 

