from django import forms
from django.contrib.auth.models import User
from .models import Comment, Category, News

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password', 'email']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'matn', 'rasm', 'bolim']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['izoh']