from django.db import models

# Create your models here.
class Car(models.Model):
    car_name=models.CharField(max_length=50)
    def __str__(self):
        return self.car_name
    
class Fule(models.Model):
    fule_name=models.CharField(max_length=50)
    car=models.ManyToManyField(Car)
    def __str__(self):
        return self.fule_name