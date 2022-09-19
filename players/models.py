from django.db import models
from teams.models import Team

# Create your models here.
class Player(models.Model):
    
    name = models.CharField(max_length=32, default="Generic player", null=False, blank=False)
    age = models.IntegerField(null=False,default=0)
    number = models.IntegerField(null=False, default=0)
    nationality = models.CharField(max_length=32,null=False,default='Generic Nationality')
    shirt_number = models.IntegerField(null=False)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self) -> str:
        return self.name