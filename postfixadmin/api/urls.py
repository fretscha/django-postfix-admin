# urls.py
from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns(
  '',
  url(r'^user/$', views.UserList.as_view()),
  url(r'^domain/$', views.DomainListOrCreate.as_view()),
  url(r'^domain/(?P<pk>\d+)/$', views.DomainDetail.as_view()),
  url(r'^alias/$', views.AliasListOrCreate.as_view()),
  url(r'^alias/(?P<pk>\d+)/$', views.AliasDetail.as_view()),
  url(r'^mailbox/$', views.MailboxListOrCreate.as_view()),
  url(r'^mailbox/(?P<pk>\d+)/$', views.MailboxDetail.as_view()),
  url(r'^vacation/$', views.VacationListOrCreate.as_view()),
  url(r'^vacation/(?P<pk>\d+)/$', views.VacationDetail.as_view()),
  url(r'^log/$', views.LogList.as_view()),
  url(r'^log/(?P<pk>\d+)/$', views.LogDetail.as_view()),
)
