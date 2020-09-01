from django.forms import ModelForm
from .models import Comment,CommentBuilder

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CommentBuilderForm(ModelForm):
    class Meta:
        model = CommentBuilder
        fields = ('body',)
