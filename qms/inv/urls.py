from django.urls import path
from . import views
app_name="inv"
urlpatterns = [
    path('',views.home,name='home'),
    path('404/',views.error,name='error'),
    path('view/<int:quiz_id>/', views.view_quiz, name="view-quiz"),
    path('create/', views.create_quiz, name="create-quiz"),
    path('view/<int:quiz_id>/<int:q_no>', views.create_question, name="create-question"),

]
