from django.forms import ModelForm, Textarea, CharField, TextInput, ImageField
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'file']

    textArgs = {'class': "form-control", 'rows': "3", 'cols': "15"}
    text = CharField(widget=Textarea(attrs=textArgs),
                     label="Ваше сообщение:")
