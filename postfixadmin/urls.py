from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

from .views import HomeView
from .views import LoginView
from .views import LogOutView

urlpatterns = [
    url('^$', HomeView.as_view(), name='home'),

    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),

    url(r'^api/', include('api.urls')),

    url(r'^pfa/', include('pfa.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
