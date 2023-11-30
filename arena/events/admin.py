from django.contrib import admin
from .models import Event,EventRegistration

# Register your models here.
class AdminEvent(admin.ModelAdmin):
    list_display = ('id','title', 'description',  'location','event_time', 'username')
admin.site.register(Event,AdminEvent)
class AdminEventRegistration(admin.ModelAdmin):
    list_display=('eid','registration_at','username')
admin.site.register(EventRegistration,AdminEventRegistration)