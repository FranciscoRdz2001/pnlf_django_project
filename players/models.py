from django.db import models

# Create your models here.
class Player(models.Model):
    number = models.IntegerField(null=False, default=0)
    name = models.CharField(max_length=32, default="Generic player", null=False, blank=False)
    age = models.IntegerField(null=False)
    nationality = models.CharField(max_length=32,null=False)
