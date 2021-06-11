from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class UserProfile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jawatan = models.CharField(max_length=50, null=True, blank=True)
    gredjawatan = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.user.first_name
