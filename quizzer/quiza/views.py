from django.contrib.auth.views import AuthenticationView, RegistrationView

from .models import Role

class QMLogin(AuthenticationView):
    def form_valid(self, form):
        user = form.get_user()
        role, _ = Role.objects.get_or_create(user=user, defaults={'role': 'QM'})
        if role.role != 'QM':
            form.add_error(None, 'You are not authorized as a Quiz Master')
            return self.form_invalid(form)
        return super().form_valid(form)

class QTLogin(AuthenticationView):
    def form_valid(self, form):
        user = form.get_user()
        role, _ = Role.objects.get_or_create(user=user, defaults={'role': 'QT'})
        if role.role != 'QT':
            form.add_error(None, 'You are not authorized as a Quiz Taker')
            return self.form_invalid(form)
        return super().form_valid(form)

class QMR(RegistrationView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.user
        Role.objects.create(user=user, role='QM')
        return response

class QTR(RegistrationView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.user
        Role.objects.create(user=user, role='QT')
        return response
