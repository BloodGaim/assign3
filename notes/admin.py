from django.contrib import admin
from .models import Note, Presentation, Tag
# Register your models here.
from accounts.models import UserProfile

class NoteInline(admin.StackedInline): #Demo StackedInline vs TabularInline
    model = Note
    fields = ('title',) 
    extra = 0
    
class PresentationAdmin(admin.ModelAdmin):
    inlines = [NoteInline,]
    model = Presentation


#http://stackoverflow.com/questions/6479999/django-admin-manytomany-inline-has-no-foreignkey-to-error    
#https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models
class TaggedNoteInline(admin.TabularInline): 
    model = Note.tag.through
    extra = 0
    
class TagAdmin(admin.ModelAdmin):
    inlines = [TaggedNoteInline,]
    model = Tag

admin.site.register(Note)
admin.site.register(Tag, TagAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(UserProfile)