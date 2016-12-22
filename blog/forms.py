from django.forms import ModelForm, Textarea, CharField, TextInput
from .models import Comments, Post


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']

    textArgs = {'class': "form-control", 'rows': "3", 'cols':"15"}
    text = CharField(widget=Textarea(attrs=textArgs),
                     label="Прокомментируйте:")


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'img', 'text']

    title = CharField(widget=TextInput(attrs={'class': "form-control"}),
                     label="Название:")
    text = CharField(widget=Textarea(attrs={'class': "form-control"}),
                     label="Напишите сюда:")