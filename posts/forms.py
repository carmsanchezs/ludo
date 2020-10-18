
# Django
from django import forms

# models 
from posts.models import Post, Comment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',)
