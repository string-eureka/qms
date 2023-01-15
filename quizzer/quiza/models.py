from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=[('QM', 'Quiz Master'), ('QT', 'Quiz Taker')])
