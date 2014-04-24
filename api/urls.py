#urls.py
from django.conf.urls import url, patterns

from .views import DomainListOrCreate, DomainDetail
from .views import AliasListOrCreate, AliasDetail
from .views import MailboxListOrCreate, MailboxDetail
from .views import VacationListOrCreate, VacationDetail
from .views import LogListOrCreate, LogDetail


urlpatterns = patterns('',
    url(r'^domain/$', DomainListOrCreate.as_view()),
    url(r'^domain/(?P<pk>\d+)$', DomainDetail.as_view()),
    url(r'^alias/$', AliasListOrCreate.as_view()),
    url(r'^alias/(?P<pk>\d+)/$', AliasDetail.as_view()),
    url(r'^mailbox/$', MailboxListOrCreate.as_view()),
    url(r'^mailbox/(?P<pk>\d+)/$', MailboxDetail.as_view()),
    url(r'^vacation/$', VacationListOrCreate.as_view()),
    url(r'^vacation/(?P<pk>\d+)/$', VacationDetail.as_view()),
    url(r'^log/$', LogListOrCreate.as_view()),
    url(r'^log/(?P<pk>\d+)/$', LogDetail.as_view()),
)
