from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from .forms import RegistrationForm, LoginForm


class RegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('accounts:register')


class LoginView(FormView):

    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:register')

    def form_valid(self, form: LoginForm):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form: LoginForm):
        errors = form.errors.get_json_data()

        for msg in errors:
            messages.error(self.request, errors[msg][0]['message'])

        return super(LoginView, self).form_invalid(form)


class LogoutView(LoginRequiredMixin, RedirectView):

    url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
