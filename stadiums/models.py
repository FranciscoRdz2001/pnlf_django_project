from unicodedata import name
from django.db import models

# Create your models here.
class Stadium(models.Model):

    name = models.CharField(null=False, default='Generic Stadium', max_length=32, blank=False)
    address = models.CharField(null=False, default='Default Stadium', max_length=64, blank=False)
    phone = models.CharField(max_length=10, default="1234567890", null=True, blank=True)
    capacity = models.IntegerField(null=False, default=0)


    def __str__(self) -> str:
        return self.name
