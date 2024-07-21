from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Register User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'birth_date']

# Authenticate User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())