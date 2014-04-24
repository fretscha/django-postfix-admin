#urls.py
from django.conf.urls import url, patterns

from .views import DomainListView, AliasListView, MailboxListView, VacationListView, LogListView

urlpatterns = patterns('',
    url(r'^domain/$', DomainListView.as_view(), name='domain_list_view'),
    url(r'^alias/$', AliasListView.as_view(), name='alias_list_view'),
    url(r'^mailbox/$', MailboxListView.as_view(), name='mailbox_list_view'),
    url(r'^vacation/$', VacationListView.as_view(), name='vacation_list_view'),
    url(r'^log/$', LogListView.as_view(), name='log_list_view'),

)
