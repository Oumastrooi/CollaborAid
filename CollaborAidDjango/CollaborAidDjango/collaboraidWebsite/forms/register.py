#registration form

from django import forms

from collaboraidWebsite.models import User
from django.forms import extras

class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    email = forms.EmailField(widget=forms.widget.EmailInput,label="Email")
    
    first_name = forms.CharField(widget=forms.widget.TextInput, label="FirstName")
    middle_name = forms.CharField(widget=forms.widget.TextInput, label="MiddleName")
    last_name = forms.CharField(widget=forms.widget.TextInput, label="LastName")
    phone = forms.CharField(widget=forms.widget.TextInput, label="PhoneNumber")
    birth_date = forms.DateField(widget=extras.SelectDateWidget, label="BirthDate")
#    image = forms.URLField(blank=True, null=True)
    
    password1 = forms.CharField(widget=forms.widget.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.widget.PasswordInput,
                                label="Password (again)")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'middle_name', 'last_name', 
                  'phone', 'birth_date', 'image', 'password1', 'password2']
        
        def clean(self):
        """
        Verifies that the values entered into the password fields match
        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
#from django.forms import CharField, EmailField, BooleanField
#from django.forms.widgets import *
#from django.core.mail import send_mail, BadHeaderError

#class RegistrationForm(forms.Form):
#    name = forms.CharField(max_length=200)
#    email = forms.EmailField(unique=True)
#    affiliation = forms.CharField(max_length=200)
#    video = forms.CharField(max_length=200)
#    acceptance = forms.CharField(widget=forms.CheckboxInput, required=True)

#    def clean_acceptance(self):
#        acceptance = self.cleaned_data['acceptance']
#        if acceptance == "False":
#            raise forms.ValidationError("Term and conditions must be accepted !")
#        return acceptance

#class UserForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput)
    
#    class Meta:
#        model = User