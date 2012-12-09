from django.conf.urls import patterns, include, url

urlpatterns = patterns('imaginary_time.views',
    url(r'^$', 'poll', name='poll'),    
)
