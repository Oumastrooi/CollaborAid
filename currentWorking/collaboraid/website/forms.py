from django import forms
from website.models import UserProfile, AnEvent
from django.db.models import Q


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
class AnEventForm(forms.ModelForm):
    event_name = forms.CharField(required=True)
    picture = forms.ImageField(required=False)
    description = forms.CharField(required=True)
    volunteer_num = forms.IntegerField(required=True)

    venue = forms.CharField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    start_time = forms.TimeField(required=True)
    end_time = forms.TimeField(required=True)
    #month = forms.CharField(required=True)
    #day = forms.DateField(required=True)
    #year = forms.DateField(required=True)
    date = forms.DateField(required=True)
    
    class Meta:
        model = AnEvent
        exclude = ('volunteer',)

PARAMETER_CHOICES = (
    ('event_name', 'Event Name'),
    ('username', 'Username'),
    ('venue', 'Venue'),
    ('address', 'Address'),
)

class SearchForm(forms.Form):
    query = forms.CharField(label='Search query', max_length=255)
    parameter = forms.ChoiceField(label='Search parameter', choices=PARAMETER_CHOICES)