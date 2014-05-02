from __future__ import absolute_import

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from braces import views

from .forms import LoginForm


class HomeView(views.LoginRequiredMixin,
    generic.TemplateView
):
    template_name = 'home.html'


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


class LogOutView(views.LoginRequiredMixin,
    views.MessageMixin,
    generic.RedirectView
):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been logged out. Come back soon!")
        return super(LogOutView, self).get(request, *args, **kwargs)

