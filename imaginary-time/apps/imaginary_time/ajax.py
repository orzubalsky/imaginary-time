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
        message = "from: %s \n message: %s" % (feedback_form.cleaned_data.get('email'), feedback_form.cleaned_data.get('message'))        
        send_mail('FF | Feedback Receieved!', message, 'noreply@fantasticfutures.fm', ('youngestforever@gmail.com',))
        
        return json.dumps({'success':True})
    return json.dumps({'success':False, 'errors': feedback_form.errors})