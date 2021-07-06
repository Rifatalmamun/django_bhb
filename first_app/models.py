from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# create Musician table
class Musician(models.Model):
    #if there is no id column, django auto generate id column
    id         = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50) 
    last_name  = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
class Album(models.Model):
    #foreign key
    artist    = models.ForeignKey(Musician, on_delete=models.CASCADE) 
    name         = models.CharField(max_length=100)
    release_date = models.DateField()
    num_start    = models.IntegerField()  
    
