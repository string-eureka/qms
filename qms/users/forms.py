from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    Quizmaster = forms.BooleanField(required=False,initial=False,label='Become a QuizMaster?')
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ("username", "Quizmaster",'email', "password1", "password2")

