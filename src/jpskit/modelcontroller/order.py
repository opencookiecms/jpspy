from django.db import models

class Order(models.Model):
    o_sebutharga  = models.CharField(max_length=150, null=True, blank=True)
    o_tarikh  = models.CharField(max_length=50, null=True, blank=True)
    o_permilik  = models.CharField(max_length=150, null=True, blank=True)
    o_jenis = models.CharField(max_length=50, null=True, blank=True)