from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class movies(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    cast=models.CharField(max_length=20)
    duration=models.TimeField(default=00)
    type=models.CharField(max_length=20)
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    reviews = models.TextField(max_length=200)
    image=models.ImageField()
    

    
    
    
