from __future__ import absolute_import

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from braces import views

from .forms import RegistrationForm
from .forms import LoginForm


class HomeView(generic.TemplateView,
    views.LoginRequiredMixin
):
    template_name = 'home.html'

    login_url = reverse_lazy('login')
    raise_exception = True

class SignUpView(generic.CreateView,
    views.AnonymousRequiredMixin,
    views.FormValidMessageMixin
):
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')
    form_valid_message = 'Thank you for your registration. You will be notified by email when your account is activated.'


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')
    form_valid_message = 'Login Successful.'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(generic.RedirectView,
    views.LoginRequiredMixin,
    views.MessageMixin
):
    url = reverse_lazy('home')
    form_valid_message = ''

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been logged out. Come back soon!")
        return super(LogOutView, self).get(request, *args, **kwargs)

