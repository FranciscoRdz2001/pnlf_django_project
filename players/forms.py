from dataclasses import fields
from django.forms import ModelForm, TextInput, EmailInput

from .models import Player

class CreatePlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        
