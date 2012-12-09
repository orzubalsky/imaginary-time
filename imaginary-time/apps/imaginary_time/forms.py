from django import forms
from django.template.loader import render_to_string
from imaginary_time.models import *

class SliderWidget(forms.HiddenInput):

    def render(self,name,value,attrs=None):        
        params = {
            'id'        : 'id_' + name,
            'field_name': name,
        }
        return render_to_string('widgets/slider.html', params)
         
class ResponseForm(forms.ModelForm):
    class Meta: 
        model   = Response
        fields  = ('dream', 'make', 'learn', 'teach', 'rest', 'taste', 'play', 'earn', 'spend', 'connect', 'move', 'help')
        widgets = {
            'dream'   : SliderWidget(attrs={'class': 'sliderInput'}),
            'make'    : SliderWidget(attrs={'class': 'sliderInput'}),
            'learn'   : SliderWidget(attrs={'class': 'sliderInput'}),
            'teach'   : SliderWidget(attrs={'class': 'sliderInput'}),
            'rest'    : SliderWidget(attrs={'class': 'sliderInput'}),
            'taste'   : SliderWidget(attrs={'class': 'sliderInput'}),
            'play'    : SliderWidget(attrs={'class': 'sliderInput'}),
            'earn'    : SliderWidget(attrs={'class': 'sliderInput'}),
            'spend'   : SliderWidget(attrs={'class': 'sliderInput'}),
            'connect' : SliderWidget(attrs={'class': 'sliderInput'}),
            'move'    : SliderWidget(attrs={'class': 'sliderInput'}),
            'help'    : SliderWidget(attrs={'class': 'sliderInput'}),
        }        