from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=12)
#     password = forms.CharField(widget=forms.PasswordInput())