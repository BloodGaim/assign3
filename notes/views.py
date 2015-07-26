from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Note
import re
from django.views.generic import ListView
from django.db.models import Q
from notes.forms import NoteForm
from .models import Presentation
from notes.forms import PresentationForm
from .models import Tag
from notes.forms import TagForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy



# Create your views here.
"""
def notes_all(request):
    allnotes = Note.objects.all()
    total = allnotes.count()
    return render(request, 'notes/index.html', {'notes': allnotes, 'total':total}) 

def note(request, note_id):
    note = Note.objects.get(id=note_id)   
    return render(request, 'notes/note.html', {'note':note})


# Create your views here.

def notes_list(request, presentation):
    if presentation == "":
        allnotes = Note.objects.all().order_by("presentation__title")
        total = allnotes.count()
    else:
        allnotes = Note.objects.filter(presentation__title__iexact=presentation)
        total = allnotes.count();
    return render(request, 'notes/index.html', {'notes': allnotes, 'total':total})  
"""

def notes_tags(request, tags):
    pieces = tags.split('/')
    # allnotes = Note.objects.none() #required when doing normal filter pipe query ... see below
    for p in pieces:
        #This is to combine results from different querysets from SAME model using normal pipe
        #https://groups.google.com/forum/#!topic/django-users/0i6KjzeM8OI
        #If the querysets are from different models, have to use itertools
        #http://chriskief.com/2015/01/12/combine-2-django-querysets-from-different-models/
        #allnotes = allnotes | Note.objects.filter(tag__title__iexact=p) # can have duplicates ... need another method
        
        #http://stackoverflow.com/questions/852414/how-to-dynamically-compose-an-or-query-filter-in-django
        # Turn list of values into list of Q objects
        queries = [Q(tag__title__iexact=value) for value in pieces]
        # Take one Q object from the list
        query = queries.pop()
        # Or the Q object with the ones remaining in the list
        for item in queries:
            query |= item
        # Query the model
        allnotes = Note.objects.filter(query).distinct().order_by('presentation__title')
        total = allnotes.count();
    return render(request, 'notes/index.html', {'pieces':pieces, 'notes': allnotes, 'total':total})   


class NoteList(ListView):
    #https://docs.djangoproject.com/en/1.7/topics/class-based-views/generic-display/
    model = Note
    
    def get_queryset(self):
        presentation = self.kwargs['presentation']
        if presentation == '':
            return Note.objects.all()
        else:
            return Note.objects.filter(presentation__title__iexact=presentation)
            
class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm

class PresentationCreate(CreateView):
    model = Presentation
    form_class = PresentationForm

class TagCreate(CreateView):
    model = Tag
    form_class = TagForm

class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm

class NoteDetail(DetailView):
    model = Note

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes_list')
