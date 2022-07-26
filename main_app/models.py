from datetime import datetime
from django.db import models
from django.urls import reverse

# Create your models here.


class Weapon(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    type=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weapon_detail', kwargs={'weapon_id': self.id})
        
class Character(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    status=models.CharField(max_length=100)
    power_level=models.IntegerField()
    weapons =models.ManyToManyField(Weapon)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'character_id': self.id})


class Battles(models.Model):
    class Meta:
        ordering =['-date']

    RESULTS=(
        ('W','Win'),
        ('L','Loss'),
        ('T','Tie'),
    )
    date=models.DateField('Battle Date')
    result=models.CharField(
        max_length=1, 
        choices=RESULTS, 
        default=RESULTS[0][0],
        )
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_result_display()} on {self.date} "