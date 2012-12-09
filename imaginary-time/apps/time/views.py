from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from time.models import *
from time.forms import *

def index(request):
    form = ResponseForm()

    return render_to_response(
        'index.html', { 
            'form' : form,
        }, context_instance=RequestContext(request))