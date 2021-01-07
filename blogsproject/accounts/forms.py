from django import forms
from .models import BlogUser

class BlogUserForm(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = ['username', 'password',]

class BlogUserCreateForm(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = ['username', 'user_id', 'user_phone', 'password',]