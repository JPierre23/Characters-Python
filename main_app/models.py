from django.db import models
from django.urls import reverse

# Create your models here.

class Character(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    status=models.CharField(max_length=100)
    power_level=models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'character_id': self.id})

class Weapon(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    type=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weapon_detail', kwargs={'weapon_id': self.id})