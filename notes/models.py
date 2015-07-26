from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True) #not a required field
    expected_time_needed_for_slide = models.CharField(max_length = 50, default = "0 Minutes")
    color = models.CharField(max_length=50, default="yellow")
    fontcolor = models.CharField(max_length=50, default="black")
    #folder is optional
    presentation = models.ForeignKey('Presentation', related_name= "notes", null=True, blank=True)
    #tag is optional
    tag = models.ManyToManyField('Tag', related_name='notes', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})
        

class Presentation(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default="purple")
    fontcolor = models.CharField(max_length=50, default="white")
    time = models.DateTimeField(null=True, blank=True) #due datetime is optional
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    done = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("notes_list")
        
class Tag(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default="red")
    fontcolor = models.CharField(max_length=50, default="black")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("notes_list")
