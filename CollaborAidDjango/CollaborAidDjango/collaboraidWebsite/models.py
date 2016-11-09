from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

# Note to self:
#   null=True sets NULL (versus NOT NULL) on the column in your DB. Blank values for Django field types such as DateTimeField or ForeignKey
#   will be stored as NULL in the DB.
#
#   blank=True determines whether the field will be required in forms. This includes the admin and your own custom forms. If blank=True then 
#   the field will not be required, whereas if it's False the field cannot be blank.


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=128, blank=False)
    middle_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    birth_date = models.DateField(blank=False)
    email = models.EmailField('email address', unique=True, blank=False)
    image = models.URLField(blank=True, null=True)
    joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email
    
class Event(models.Model):
    name = models.TextField(max_length=60, blank=False)
    date = models.DateField(blank=False)
    description = models.TextField(max_length=1000, blank=False)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    start_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)
    venue = models.ForeignKey(Venue)

    def __unicode__(self):
        return self.name

class Venue(models.Model):
    venue_name = models.TextField(max_length=60, blank=False)
    street_address = models.TextField(max_length=60, blank=False)
    city = models.CharField(max_length=20, blank=False)
    zip_code = models.IntegerField(max_length=5, blank=False)

    def __unicode__(self):
        return self.venue_name
