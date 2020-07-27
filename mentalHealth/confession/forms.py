from .models import Post
from django import forms

class post_form (forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['body']
