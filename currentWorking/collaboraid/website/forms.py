from django import forms
from website.models import UserProfile

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
class EventRegistrationForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    date = forms.DateTimeField(required=True)
    start_time = forms.TimeField(required=True)
    end_time = forms.TimeField(required=True)
    venue = forms.CharField(required=True)
    picture = forms.ImageField(required=False)