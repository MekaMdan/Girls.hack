from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Student

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ('password')

