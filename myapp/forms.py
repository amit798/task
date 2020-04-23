from django import forms
from django.forms import ModelForm
from django.forms.utils import ValidationError
from .models import Employee
import re
class EmplyoeeForm(forms.ModelForm):
    class Meta:
        model=Employee

        fields=['name','pan_number','age','gender','email','city']

    """def clean_name(self):
        name=self.cleaned_data.get('name')
        if not re.match("^[a-zA-Z\s]*$",name):
            raise ValidationError('only alphabet characters are allowed..')
        return name

    def clean_pan_number(self):
        pan_number=self.cleaned_data.get('pan_number')
        if not re.match(r'^[A-Za-z]{5}[0-9]{4}[A-Za-z]$',pan_number):
            raise ValidationError('Please provide valid Pan number or Only alphanumeric characters are allowed and pan number must be uniques....')
        return pan_number """

class EmployeeSearchForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields= ['name']