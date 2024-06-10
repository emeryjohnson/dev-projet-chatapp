# LA STRUCTURE DE APPLICATION
from django.db import models
from datetime import datetime


# Create your models here.

# class room qui represente le groupe 

class Room(models.Model):
    name = models.CharField(max_length=2000)

#class message pour écrit le message     

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date =  models.DateTimeField(default = datetime.now , blank=True)
    user = models.CharField(max_length=1000000)
    room =  models.CharField(max_length=1000000)
    