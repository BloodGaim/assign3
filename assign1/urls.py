from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import views

urlpatterns = patterns('',
    url(r'^list/$', views.notes_all, name='notes_list'),
    url(r'^note/(?P<note_id>\d+)$', views.note, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/(?P<presentation>.*)$', views.notes_list, name='notes_list'),
    url(r'^tag/(?P<tags>.*)$', views.notes_tags, name='notes_list'),

 

)