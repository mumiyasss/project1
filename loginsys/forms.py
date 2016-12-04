from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as before, for verification."))
