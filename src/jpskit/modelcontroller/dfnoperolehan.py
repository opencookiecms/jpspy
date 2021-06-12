from django.db import models
from django.contrib.auth.models import User
from ..modelcontroller import userprofile
import uuid


class NoPerolehan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    noperolehan = models.CharField(max_length=100, null=True, blank=True, unique=True)
    tarikh  = models.DateField(null=True, blank=True)
    kaedahperolehan  = models.CharField(max_length=50, null=True, blank=True)
    pegawaiselia = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.noperolehan
