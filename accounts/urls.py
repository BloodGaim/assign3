from django.conf.urls import *
from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^login/$', login, {'template_name':'accounts/login.html'},name='login'), 
    url(r'^logout/$', logout, {'next_page':'/'},name='logout'), 
    url(r'^register/$', 'accounts.views.registration',name='register'), 
)
