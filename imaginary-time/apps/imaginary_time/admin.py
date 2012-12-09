from imaginary_time.models import *
from django.contrib import admin

class ResponseAdmin(admin.ModelAdmin):
    list_display        = ('sent_by', 'dream', 'make', 'learn', 'teach', 'rest', 'taste', 'play', 'earn', 'spend', 'connect', 'move', 'help')
    fields              = ('sent_by', 'dream', 'make', 'learn', 'teach', 'rest', 'taste', 'play', 'earn', 'spend', 'connect', 'move', 'help')

admin.site.register(Response, ResponseAdmin)