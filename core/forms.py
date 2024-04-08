from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text':forms.Textarea(attrs={
                'class':'w-full px-6 py-4 border border-slate-300 rounded-xl'
            })
        }