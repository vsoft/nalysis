from django import forms
import datetime

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'rows': 2, 'cols': 2}))
    content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 4, 'cols': 4}))