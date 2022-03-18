from tkinter import CASCADE
from django.db import models
import supers_types
from supers_types.models import SuperType
# Create your models here.
class Super(models.Model):
    name= models.CharField(max_length=255)
    alter_ego= models.CharField(max_length=255)
    primary_ability= models.CharField(max_length=255)
    secondary_ability= models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    supers_types_id = models.ForeignKey(SuperType, on_delete=models.CASCADE) 

