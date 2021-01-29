from django.db import models
from ..modelcontroller import document,dfnoperolehan,kontraktor




class MRKKursus(models.Model):
    kscode = models.CharField(max_length=50, null=True, blank=True)
    ksname = models.CharField(max_length=100, null=True, blank=True)

class MRKSatu(models.Model):

    mrksatunoinden = models.CharField(max_length=50, null=True, blank=True)
    mrksatugred = models.CharField(max_length=20, null=True, blank=True)
    mrksatukategori  = models.CharField(max_length=20, null=True, blank=True)
    mrksatupengkhususan = models.CharField(max_length=100, null=True, blank=True)
    mrksatutarikhmula = models.CharField(max_length=50, null=True, blank=True)
    mrksatutarikhjangkasiap = models.CharField(max_length=50, null=True, blank=True)
    mrksatukosprojek = models.CharField(max_length=100, null=True, blank=True)
    mrksatutarikhdaftar = models.CharField(max_length=50, null=True, blank=True)
    mrksatunosebutharga = models.ForeignKey(dfnoperolehan.NoPerolehan, blank=True, null=True, on_delete = models.SET_NULL)
    mrksatukontraktor = models.ForeignKey(kontraktor.Kontraktor, blank=True, null=True, on_delete = models.SET_NULL)

    
    class Meta: 
        # Add verbose name 
        verbose_name_plural = 'MRK 1'

class MRKDua(models.Model):
    
    mrkduakerjajadual = models.CharField(max_length=50, null=True, blank=True)
    mrkduakerjasebenartarikh = models.CharField(max_length=50, null=True, blank=True)
    mrkduakerjasebenar = models.CharField(max_length=50, null=True, blank=True)
    mrkduakemajuan = models.CharField(max_length=50, null=True, blank=True)
    mrkduabayarankemajuan = models.CharField(max_length=50, null=True, blank=True)
    mrkduamodal = models.CharField(max_length=50, null=True, blank=True)
    mkrduabahan = models.CharField(max_length=50, null=True, blank=True)
    mrkduapekerja = models.CharField(max_length=50, null=True, blank=True)
    mrkduatapak = models.CharField(max_length=50, null=True, blank=True)
    mrkduacuaca = models.CharField(max_length=50, null=True, blank=True)
    mrkduadisebabkanoleh = models.CharField(max_length=200, null=True, blank=True)
    mrkdualainlain = models.CharField(max_length=200, null=True, blank=True)
    mrkdualanjutmasa = models.CharField(max_length=50, null=True, blank=True)
    mrkdualanjutdari = models.CharField(max_length=50, null=True, blank=True)
    mrkdualanjutsehingga = models.CharField(max_length=50, null=True, blank=True)
    mrkduadisebabkan = models.CharField(max_length=200, null=True, blank=True)
    mrkduaLAD = models.CharField(max_length=50, null=True, blank=True)
    mrkduaLADdari = models.CharField(max_length=50, null=True, blank=True)
    mrkduaLADSehingga = models.CharField(max_length=50, null=True, blank=True)
    mrkduaperakuan = models.CharField(max_length=50, null=True, blank=True)
    mrkduamansuh = models.CharField(max_length=50, null=True, blank=True)
    mrkduatarikhlaporan = models.CharField(max_length=50, null=True, blank=True)
    mrkduanosebutharga  = models.ForeignKey(dfnoperolehan.NoPerolehan, blank=True, null=True, on_delete = models.SET_NULL)
    mrksatulink = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)

    class Meta: 
        # Add verbose name 
        verbose_name_plural = 'MRK 2'


class Laporansiapkerja(models.Model):
    
    lskhargasebenar  = models.CharField(max_length=50, null=True, blank=True)
    lsklanjutmasa  = models.CharField(max_length=50, null=True, blank=True)
    lskkerjasiap  = models.CharField(max_length=50, null=True, blank=True)
    lskperuntukan  = models.CharField(max_length=50, null=True, blank=True)
    lsklaporan  = models.CharField(max_length=200, null=True, blank=True)
    lsktarikhperakui  = models.CharField(max_length=50, null=True, blank=True)
    lskketuabahagian  = models.CharField(max_length=50, null=True, blank=True)
    lskjawatanketuabahagian  = models.CharField(max_length=50, null=True, blank=True)
    lskjuruteraj41  = models.CharField(max_length=50, null=True, blank=True)
    lskjawatanj41  = models.CharField(max_length=50, null=True, blank=True)
    lskjuruteradaerah  = models.CharField(max_length=50, null=True, blank=True)
    lskjawatanjuruteradaerah  = models.CharField(max_length=50, null=True, blank=True)
    lskperkeso  = models.CharField(max_length=50, null=True, blank=True)
    lskjenisinsurancesatu  = models.CharField(max_length=50, null=True, blank=True)
    lsknoinsurancesatu  = models.CharField(max_length=50, null=True, blank=True)
    lskjenisinsurancedua  = models.CharField(max_length=50, null=True, blank=True)
    lsknoinsurancedua  = models.CharField(max_length=50, null=True, blank=True)
    lsknosebutharga  = models.CharField(max_length=50, null=True, blank=True)
    lskmrksatulink  = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Laporan Siap Kerja'


class MRKTiga(models.Model):
    pass








