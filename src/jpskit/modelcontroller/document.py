from django.db import models
from ..modelcontroller import dfnoperolehan

class MRK1(models.Model):

    noinden = models.CharField(max_length=50, null=True, blank=True)
    gred = models.CharField(max_length=20, null=True, blank=True)
    kategori  = models.CharField(max_length=20, null=True, blank=True)
    pengkhususan = models.CharField(max_length=100, null=True, blank=True)
    tarikhmula = models.CharField(max_length=50, null=True, blank=True)
    tarikhjangkasiap = models.CharField(max_length=50, null=True, blank=True)
    pegawai  = models.CharField(max_length=100, null=True, blank=True)
    jawatan  = models.CharField(max_length=50, null=True, blank=True)
    kosprojek = models.CharField(max_length=100, null=True, blank=True)
    tarikhdaftar = models.CharField(max_length=50, null=True, blank=True)
    nosebutharga = models.ForeignKey(dfnoperolehan.NoPerolehan, on_delete=models.CASCADE)

class MRK2(models.Model):
    pass


