from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    Quizmaster = forms.BooleanField(required=False,initial=False,label='Become a QuizMaster?')
    class Meta:
        model = User
        fields = ("username", "Quizmaster", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    Quizmaster = forms.BooleanField(required=False,initial=False)
    class Meta:
        model = User
        fields = ("username", "Quizmaster")