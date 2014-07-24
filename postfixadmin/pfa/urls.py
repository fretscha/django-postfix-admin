# urls.py
from __future__ import absolute_import

from django.conf.urls import patterns, include, url

from . import views

domain_patterns = patterns(
    '',
    url(r'^$', views.DomainListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.DomainDetailView.as_view(), name='detail'),
)

alias_patterns = patterns(
    '',
    url(r'^$', views.AliasListView.as_view(), name='list'),
)

mailbox_patterns = patterns(
    '',
    url(r'^$', views.MailboxListView.as_view(), name='list'),
)

vacation_patterns = patterns(
    '',
    url(r'^$', views.VacationListView.as_view(), name='list'),
)

log_patterns = patterns(
    '',
    url(r'^$', views.LogListView.as_view(), name='list'),
)


urlpatterns = patterns('',
                       url(r'^$', views.DashboardView.as_view(),
                           name='dashboard'),
                       url(r'^domain/',
                           include(domain_patterns, namespace='domain')),
                       url(r'^alias/',
                           include(alias_patterns, namespace='alias')),
                       url(r'^mailbox/',
                           include(mailbox_patterns, namespace='mailbox')),
                       url(r'^vacation/',
                           include(vacation_patterns, namespace='vacation')),
                       url(r'^log/', include(log_patterns, namespace='log')),
                       )
