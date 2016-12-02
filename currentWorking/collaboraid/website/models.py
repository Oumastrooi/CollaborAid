from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username
    
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default= '')
    date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='event_images', blank=True)
    volunteer_num = models.IntegerField(default=1)
    
    event_owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __unicode__(self):
        return self.title