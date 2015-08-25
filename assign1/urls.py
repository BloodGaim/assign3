from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import views
from django.views.generic import ListView
from notes.models import Note

from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/(?P<presentation>.*)$', views.NoteList.as_view(), name='notes_list_presentation'),
    url(r'^tag/(?P<tags>.*)$', views.notes_tags, name='notes_list_tag'),
    url(r'^$', ListView.as_view(model=Note), name='notes_list'),
    url(r'^addnote/$', views.NoteCreate.as_view(), name='note_add'),
    url(r'^addpresentation/$', views.PresentationCreate.as_view(), name='presentation_add'),
    url(r'^addtag/$', views.TagCreate.as_view(), name='tag_add'),
    url(r'^note/(?P<pk>\d+)/edit/$', views.NoteUpdate.as_view(),  name='note_update'),
    url(r'^note/(?P<pk>\d+)$', views.NoteDetail.as_view(),  name='detail'),
    url(r'^note/(?P<pk>\d+)/delete/$', views.NoteDelete.as_view(),  name='note_delete'),
    url(r'^accounts/', include('accounts.urls')),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),

)