from django.db import models


class sistemsetup(models.Model):
    namajabatan = models.CharField(max_length=150, null=True, blank=True)
    alamatjabatan = models.CharField(max_length=200, null=True, blank=True)
    slogan1 = models.CharField(max_length=150, null=True, blank=True)
    slogan2 = models.CharField(max_length=150, null=True, blank=True)
    logo = models.FileField(null=True, blank=True)


