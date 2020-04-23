from django.db import models
from django.shortcuts import reverse
from django.core.exceptions import ValidationError
import re
# Create your models here.
GENDERS=(
    ('','Gender'),
    ('M','Male'),
    ('F','Female'),
)
def validate_pan_number(value):
    if not re.match(r'^[A-Za-z]{5}[0-9]{4}[A-Za-z]$', value):
        raise ValidationError(
            'Please provide valid Pan number or Only alphanumeric characters are allowed and pan number must be uniques....')
    return value

def validate_name(value):
    if not re.match("^[a-zA-Z\s]*$", value):
        raise ValidationError('only alphabet characters are allowed..')
    return value
class Employee(models.Model):
    name=models.CharField(max_length=200,validators=[validate_name])
    pan_number=models.CharField(max_length=20,unique=True,validators=[validate_pan_number])
    age=models.CharField(max_length=5)
    gender=models.CharField(max_length=1,choices=GENDERS,null=True)
    email=models.EmailField(max_length=100)
    city=models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee',kwargs={'pk':self.pk})

