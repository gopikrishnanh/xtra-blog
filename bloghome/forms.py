from django import forms
from .models import Post


class postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body','img')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'},
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog'}),
        }
