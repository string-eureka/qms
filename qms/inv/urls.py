from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('404/',views.error,name='error'),
    path('view/<int:quiz_id>', views.view_quiz, name="view-quiz")

]
