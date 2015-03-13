from django.views import generic
from django.contrib.auth.models import User
from braces import views

from . import models
from . import forms


class DashboardView(
    views.LoginRequiredMixin,
    generic.TemplateView
):
    template_name = "pfa/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['domain_count'] = models.Domain.objects.count()
        context['alias_count'] = models.Alias.objects.count()
        context['mailbox_count'] = models.Mailbox.objects.count()
        # active  vs inacctive
        # activated vacations
        #
        # messages recieved
        # messages sent
        # messages rejected
        # messages quarantained
        return context


class SearchView(
    views.LoginRequiredMixin,
    generic.TemplateView
):

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        # context['domain'] = models.Domain.objects.get(
        #     pk=self.kwargs.get('taskid', None))
        return context


class DomainListView(
    views.LoginRequiredMixin,
    generic.ListView
):
    model = models.Domain


class DomainDetailView(
    views.LoginRequiredMixin,
    generic.DetailView
):
    model = models.Domain


class AliasListView(generic.ListView):
    model = models.Alias


class MailboxListView(generic.ListView):
    template_name = "mailbox_list.html"
    model = models.Mailbox


class VacationListView(generic.ListView):
    model = models.Vacation


class LogListView(generic.ListView):
    model = models.Log
