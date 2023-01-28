from django import forms
from .models import Question, Quiz

class AddQuiz(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ("quiz_title", "quiz_desc")

class AddQuestion(forms.ModelForm):

    class Meta:
        model = Question
        fields = ("prompt", "type","points","pen")
        widgets = {"type": forms.RadioSelect(choices=[("MCQ", "Multiple Choice Question"),("INT", "Integer Type"),("BIN", "True-False"),("MLT", "Multiple Correct Type"),])}