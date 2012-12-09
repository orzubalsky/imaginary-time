from django.template.loader import render_to_string
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.utils import simplejson as json
from django.utils.safestring import mark_safe
from django.core.mail import mail_admins, send_mail
from imaginary_time.forms import *


@dajaxice_register(method='POST')
def submit_form(request, form):
    
    response_form = ResponseForm(deserialize_form(form))
        
    if response_form.is_valid():
        valid_form = response_form.save(commit=False)            
        valid_form.sent_by = get_client_ip(request)
        valid_form.save()
        
        return json.dumps({'success':True})
    return json.dumps({'success':False, 'errors': response_form.errors})
        
    
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip