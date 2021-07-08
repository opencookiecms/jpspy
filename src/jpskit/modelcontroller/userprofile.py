from typing import no_type_check
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jawatan = models.CharField(max_length=50, null=True, blank=True)
    gredjawatan = models.CharField(max_length=50, null=True, blank=True)
    batchno = models.CharField(max_length=50, null=True, blank=True) 
    nokp = models.CharField(max_length=50, null=True, blank=True)
    groupunit = models.CharField(max_length=50, null=True, blank=True)
    unitsokongan = models.CharField(max_length=50, null=True, blank=True)
    gambar = models.FileField(null=True, blank=True);
    
    def __str__(self):
        return self.user.first_name
