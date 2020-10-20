from django.db import models

# Create your models here.
class Kontraktor(models.Model):
    
    konNama = models.CharField(max_length=100, blank=True)
    konImage = models.CharField(max_length=150, blank=True)
    konAlamat = models.CharField(max_length=200, blank=True)

class Projek:
    pass

class MR1:
    pass

class MR2:
    pass

class MR3:
    pass
