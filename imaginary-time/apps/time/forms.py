from django import forms
from time.models import *

class ResponseForm(forms.ModelForm):
    class Meta: 
        model   = Response
        fields  = ['dream', 'make', 'learn', 'teach', 'rest', 'taste', 'play', 'earn', 'spend', 'connect', 'move', 'help']