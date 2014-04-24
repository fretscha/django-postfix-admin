from django.shortcuts import render
from django.views.generic import ListView

from .models import Alias, Domain, Log, Mailbox, Vacation

class DomainListView(ListView):
    template_name = "index.html"
    model = Domain

class AliasListView(ListView):
    model = Alias

class MailboxListView(ListView):
    model = Mailbox

class VacationListView(ListView):
    model = Vacation

class LogListView(ListView):
    model = Log
