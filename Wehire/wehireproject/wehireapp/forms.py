from django import forms
from django.contrib.auth.models import User
from .models import *


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows':3,'cols':30}))





class postjobform(forms.Form):


    Jobtitle = forms.CharField(max_length=30)
    companyname = forms.CharField(max_length=30)
    jobdescription = forms.CharField(max_length=255)
    Experience = forms.CharField(max_length=30)
    workplace = forms.CharField(max_length=30)
    Employmenttype = forms.CharField(max_length=30)


