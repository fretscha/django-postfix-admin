from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'postfixadmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^pfa/', include('pfa.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
