from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from .managers import UserManager

import os

# Create your models here.

# Note to self:
#   null=True sets NULL (versus NOT NULL) on the column in your DB. Blank values for Django field types such as DateTimeField or ForeignKey
#   will be stored as NULL in the DB.
#
#   blank=True determines whether the field will be required in forms. This includes the admin and your own custom forms. If blank=True then 
#   the field will not be required, whereas if it's False the field cannot be blank.


'''class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True, blank=False)
    first_name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    birth_date = models.DateField(blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
        
    avatar = models.ImageField(upload_to='avatars/', blank=False, null=True)
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'birth_date', 'avatar']
    
    def __unicode__(self):
        return self.email
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # Returns the full name for the user
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    # Returns the short name for the user
    def get_short_name(self):
        return self.first_name

    # Sends an email to this user
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
'''
    
class UserManager(BaseUserManager):
    use_in_migrations = True

    # Creates and saves a User with the given email and password
    def _create_user(self, email, password, first_name, last_name, 
                     phone, birth_date, avatar):
        if not email:
            raise ValueError('The given email must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, 
                          last_name=last_name, phone=phone, birth_date=birth_date, avatar=avatar)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, first_name, last_name, 
                     phone, birth_date, avatar):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, 
                     phone, birth_date, avatar)

    def create_superuser(self, email, password, first_name, last_name, 
                     phone, birth_date, avatar):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, 
                     phone, birth_date, avatar)
        
class Venue(models.Model):
    venue_name = models.TextField(max_length=60, blank=False)
    street_address = models.TextField(max_length=60, blank=False)
    city = models.CharField(max_length=20, blank=False)
    zip_code = models.CharField(max_length=5, blank=False)

    def __unicode__(self):
        return self.venue_name

    
class Event(models.Model):
    name = models.TextField(max_length=60, blank=False)
    date = models.DateField(blank=False)
    description = models.TextField(max_length=1000, blank=False)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    start_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)
    venue = models.ForeignKey(Venue)
    event_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
    
    event_image = models.ImageField(upload_to='avatars/', blank=True, null=True)
