from dataclasses import fields
from django.forms import ModelForm, TextInput, EmailInput

from .models import Stadium

class CreateStadiumForm(ModelForm):
    class Meta:
        model = Stadium
        fields = '__all__'
        
