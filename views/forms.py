from django import forms
from .models import Post


# 1. Standart Form (Oddiy form misoli)
class PostForm(forms.Form):
    title = forms.CharField(max_length=200, label="Sarlavha")
    content = forms.CharField(widget=forms.Textarea, label="Maqola matni")

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Sarlavha kamida 5 ta belgidan iborat bo'lishi kerak!")
        return title


# 2. ModelForm (Model bilan to'g'ridan-to'g'ri ishlovchi form)
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sarlavhani kiriting...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Matnni kiriting...'}),
        }

    # Custom validatsiya misoli
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "reklama" in title.lower():
            raise forms.ValidationError("Reklama mazmunidagi sarlavhalar taqiqlanadi!")
        return title
