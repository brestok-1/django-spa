from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': "3",
    }))

    class Meta:
        model = Comment
        fields = ('text',)


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'placeholder': 'Your name',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': 'Your email',
    }))
    theme = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'subject',
        'placeholder': 'Theme',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'message',
        'placeholder': 'Theme',
        'rows': 4
    }))
