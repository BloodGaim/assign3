from django import forms
from .models import Note
from .models import Presentation 
from .models import Tag
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class NoteForm(forms.ModelForm):
    class Meta: 
        model = Note
        
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))
    
class PresentationForm(forms.ModelForm):
    class Meta: 
        model = Presentation
        
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))

class TagForm(forms.ModelForm):
    class Meta: 
        model = Tag
        
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))

