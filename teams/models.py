from django.db import models

# Create your models here.
class Team(models.Model):

    name = models.CharField(default='No name', null=False, blank=False, max_length=64)
    trainer = models.CharField(default='No trainer', null=False, blank=False, max_length=64)
    players_quantity = models.IntegerField(null=False)

