from django.conf.urls import patterns, include, url

urlpatterns = patterns('time.views',
    url(r'^$', 'index', name='home'),    
)
