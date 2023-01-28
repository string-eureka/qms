from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Quizmaster = models.BooleanField(default=False)
    email = models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.username