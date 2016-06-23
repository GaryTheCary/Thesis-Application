from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^client/', include('client.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
