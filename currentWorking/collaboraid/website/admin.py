from django.contrib import admin
from website.models import UserProfile, AnEvent

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'venue', 'date', 'start_time', 'end_time')
    search_fields = ('event_name', )


admin.site.register(UserProfile)
admin.site.register(AnEvent, EventAdmin)
