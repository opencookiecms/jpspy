from django.db import models
from django.contrib.auth.models import User


class NoPerolehan(models.Model):
    noperolehan = models.CharField(max_length=100, null=True, blank=True)
    tarikh  = models.CharField(max_length=50, null=True, blank=True)
    kaedahperolehan  = models.CharField(max_length=50, null=True, blank=True)
    pegawaiselia  = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.noperolehan