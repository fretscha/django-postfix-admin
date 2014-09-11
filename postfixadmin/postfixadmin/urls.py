from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

from .views import HomeView
from .views import LoginView
from .views import LogOutView

urlpatterns = [
    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('pfa:dashboard'), permanent=True), name='home'),

    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),

    url(r'^api/', include('api.urls', namespace='api')),

    url(r'^pfa/', include('pfa.urls', namespace='pfa')),

    url(r'^admin/', include(admin.site.urls)),
]
