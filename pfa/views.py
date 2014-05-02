from django.views import generic

from braces import views

from . import models
from . import forms


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
