from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$',views.login, name='login'),
    url(r'^app$', views.app, name='app'),
    url(r'^product', views.product, name='product'),
    url(r'^view', views.m_view, name='view'),
    url(r'^ajax/post/$', views.postNotification, name='postNotification'),
    url(r'^notification', views.notification, name='notification'),
    # url(r'^signup', views.signup, name='signup'),

    #validate the login form

    url(r'^validation', views.validation, name='validation'),

    # Get more field in notification
]