from dataclasses import fields
from django.forms import ModelForm, TextInput, EmailInput

from .models import Team

class CreateTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        
