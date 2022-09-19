from django.db import models
from stadiums.models import Stadium

# Create your models here.
class Team(models.Model):

    name = models.CharField(default='No name', null=False, blank=False, max_length=64)
    trainer = models.CharField(default='No trainer', null=False, blank=False, max_length=64)
    players_quantity = models.IntegerField(default=0, null=True, blank=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
