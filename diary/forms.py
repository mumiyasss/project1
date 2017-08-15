from .models import DiaryPage
from django.forms import ModelForm, Textarea, CharField, TextInput, ImageField

class NewPageForm(ModelForm):
	class Meta:
		model = DiaryPage
		fields = ['text_rich']