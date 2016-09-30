from django import forms

class checkForm(forms.Form):
    answer = forms.CharField(max_length=100);
