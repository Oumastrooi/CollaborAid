from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name', 'email']
	
admin.site.register(User, UserAdmin)

class VenueAdmin(admin.ModelAdmin):
	list_display = ['venue_name', 'city']

admin.site.register(Venue, VenueAdmin)