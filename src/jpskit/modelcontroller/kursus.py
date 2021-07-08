from os import O_NDELAY
from typing import SupportsIndex
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    tajukkursus = models.CharField(max_length=300, null=True, blank=True)
    tarikhmula =  models.DateField(null=True, blank=True)
    tarikhakhir =  models.DateField(null=True, blank=True)
    tempat = models.CharField(max_length=150, null=True, blank=True)
    tahun = models.CharField(max_length=10, null=True, blank=True)
    hari = models.CharField(max_length=10, null=True, blank=True)
    

class Attandance(models.Model):
    one = models.IntegerField(blank=True, null=True)
    two  = models.IntegerField(blank=True, null=True)
    three = models.IntegerField(blank=True, null=True)
    four  = models.IntegerField(blank=True, null=True)
    five = models.IntegerField(blank=True, null=True)
    six  = models.IntegerField(blank=True, null=True)
    seven  = models.IntegerField(blank=True, null=True)
    eight = models.IntegerField(blank=True, null=True)
    projekbind = models.ForeignKey(Course, blank=True, null=True, on_delete = models.SET_NULL)
   
  