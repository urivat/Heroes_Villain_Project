from tkinter import CASCADE
from django.db import models
from supers_types import superTypes
# Create your models here.
class Supers(models.Models):
    name= models.CharField(max_length=255)
    alter_ego= models.CharField(max_length=255)
    primary_ability= models.CharField(max_length=255)
    secondary_ability= models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(SuperType=on_delete=models.CASCADE):
    