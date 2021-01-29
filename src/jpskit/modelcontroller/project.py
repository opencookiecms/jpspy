from django.db import models
from django.urls import reverse
from ..modelcontroller import kontraktor, dfnoperolehan


class Projek(models.Model):

    tajukkerja = models.CharField(max_length=50, null=True, blank=True)
    daerah = models.CharField(max_length=50, null=True, blank=True)
    pgred = models.CharField(max_length=50, null=True, blank=True)
    pkategori = models.CharField(max_length=50, null=True, blank=True)
    pkhususan1 = models.CharField(max_length=50, null=True, blank=True)
    pkhususan2 = models.CharField(max_length=50, null=True, blank=True)
    pkhususan3 = models.CharField(max_length=50, null=True, blank=True)
    ptaraf = models.CharField(max_length=50, null=True, blank=True)
    ptempohsiap = models.CharField(max_length=50, null=True, blank=True)
    pweekormonth = models.CharField(max_length=50, null=True, blank=True)
    hargadukumen = models.CharField(max_length=50, null=True, blank=True)
    tarikhnotis = models.CharField(max_length=50, null=True, blank=True)
    tariklawattapak = models.CharField(max_length=50, null=True, blank=True)
    tarikhdukemenjual = models.CharField(max_length=50, null=True, blank=True)
    tarikhakhirdukemenjual = models.CharField(max_length=50, null=True, blank=True)
    tarikhtutupsebutharga = models.CharField(max_length=50, null=True, blank=True)
    pjuruteradearah = models.CharField(max_length=50, null=True, blank=True)
    pjurutera = models.CharField(max_length=50, null=True, blank=True)
    pjuruterakanan36 = models.CharField(max_length=50, null=True, blank=True)
    pjurutera29 = models.CharField(max_length=50, null=True, blank=True)
    kodvot = models.CharField(max_length=50, null=True, blank=True)
    peruntukan = models.CharField(max_length=50, null=True, blank=True)
    peruntukansemasa = models.CharField(max_length=50, null=True, blank=True)
    latitud1 = models.CharField(max_length=50, null=True, blank=True)
    latitud2 = models.CharField(max_length=50, null=True, blank=True)
    latitud3 = models.CharField(max_length=50, null=True, blank=True)
    longlitud1 = models.CharField(max_length=50, null=True, blank=True)
    longlitud2 = models.CharField(max_length=50, null=True, blank=True)
    longlitud3 = models.CharField(max_length=50, null=True, blank=True)
    lembangansungai = models.CharField(max_length=50, null=True, blank=True)
    sistem = models.CharField(max_length=50, null=True, blank=True)
    subsistem = models.CharField(max_length=50, null=True, blank=True)
    komponen = models.CharField(max_length=50, null=True, blank=True)
    dimensi = models.CharField(max_length=50, null=True, blank=True)
    nosebuthargaid = models.ForeignKey(dfnoperolehan.NoPerolehan, blank=True, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.tajukkerja


class isSungai(models.Model):
    sg_name = models.CharField(max_length=50, null=True, blank=True)
    sg_cabang = models.CharField(max_length=50, null=True, blank=True)
    sg_pangjang = models.CharField(max_length=50, null=True, blank=True)
    sg_daerah = models.CharField(max_length=50, null=True, blank=True)
    sg_noshet = models.CharField(max_length=50, null=True, blank=True)
    sg_norujukan = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.sg_name

    
    class Meta: 
        # Add verbose name 
        verbose_name_plural = 'Sungai'

class sistem(models.Model):
    sistemname = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.sistemname

class subsistem(models.Model):
    subsistemname  = models.CharField(max_length=50, null=True, blank=True)
    sistemlink = models.ForeignKey(sistem, on_delete=models.CASCADE)

    def __str__(self):
        return self.subsistemname



