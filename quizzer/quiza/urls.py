from django.urls import path
from .views import QuizMasterAuthenticationView, QuizTakerAuthenticationView, QuizMasterRegistrationView, QuizTakerRegistrationView

urlpatterns = [
    path('qm/login/', QuizMasterAuthenticationView.as_view(), name='qm_login'),
    path('qm/register/', QuizMasterRegistrationView.as_view(), name='qm_register'),
    path('qt/login/', QuizTakerAuthenticationView.as_view(), name='qt_login'),
    path('qt/register/', QuizTakerRegistrationView.as_view(), name='qt_register'),
]
