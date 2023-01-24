from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User
    UserAdmin.Quizmaster=True
    list_display = ["username", "Quizmaster","email"]

admin.site.register(User, CustomUserAdmin)