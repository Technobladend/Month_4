from django import forms
from posts.models import Comment, Post, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=100)
    content = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'python':
            raise forms.ValidationError('Python title is not valid')
        else:
            return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower() == content.lower():
            raise forms.ValidationError('content and titile cant be same')
        else:
            return cleaned_data


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and title.lower() == 'python':
            raise forms.ValidationError('"Python" is not a valid title')
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        
        if title and content:
            if title.lower() == content.lower():
                raise forms.ValidationError("Content and title can't be the same.")
        
        return cleaned_data


class SearchForm(forms.Form): 
    search = forms.CharField(
        required=False,
        max_length=100,
        min_length=1,
        widget=forms.TextInput(
            attrs={'placeholder': "Search",
                   "class": "form-control"}
        )
    )
    tag = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(), 
        widget=forms.CheckboxSelectMultiple
        )
    
    ordering = (
        ("created_at", 'По дате создания'),
        ('-created_at', 'По дате создания (По убыванию)'),
        ("title", 'По названию'),
        ('-title', 'По названию (По убыванию)'),
        ("rate", 'По рейтингу'),
        ("-rate", 'По рейтингу (По убыванию)')
    )


    ordering = forms.ChoiceField(required=False, choices=ordering)
