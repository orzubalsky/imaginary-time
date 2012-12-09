from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from imaginary_time.models import *
from imaginary_time.forms import *

def poll(request):    
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            valid_form = form.save(commit=False)            
            valid_form.sent_by = get_client_ip(request)
            valid_form.save()
    else:
        form = ResponseForm()
                
    return render_to_response(
        'poll.html', { 
            'form' : form,
        }, context_instance=RequestContext(request))
        
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip