from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    jawatan = models.CharField(max_length=50, null=True, blank=True)
    gredjawatan = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.user.first_name
