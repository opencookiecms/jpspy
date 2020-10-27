from django.db import models
from django.contrib.auth.models import User
from .datacontroller import project

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    jawatan = models.CharField(max_length=50, null=True, blank=True)
    gredjawatan = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.user.first_name


class Kontraktor(models.Model):
    
    #maklumat syarikat
    konNama = models.CharField(max_length=100, null=True, blank=True)
    konImage = models.FileField(null=True, blank=True);
    konAlamat = models.CharField(max_length=200, null=True, blank=True)
    konAlamatExtS = models.CharField(max_length=50, null=True, blank=True)
    konAlamatExtD = models.CharField(max_length=20, null=True, blank=True)
    konPoskod = models.CharField(max_length=10, null=True, blank=True)
    konBandar = models.CharField(max_length=20, null=True, blank=True)
    konDaerah = models.CharField(max_length=20, null=True, blank=True)
    konNegeri = models.CharField(max_length=20, null=True, blank=True)
    konTel = models.CharField(max_length=20, null=True, blank=True)
    konEmail = models.CharField(max_length=150, null=True, blank=True)
    konFax = models.CharField(max_length=20, null=True, blank=True)
    konBank = models.CharField(max_length=50, null=True, blank=True)
    konNoAkaun = models.CharField(max_length=50, null=True, blank=True)
    konKawOperasi = models.CharField(max_length=20, null=True, blank=True)
    konPrestasi = models.CharField(max_length=10, null=True, blank=True)
    #maklumat pengurus
    konPengurus = models.CharField(max_length=150, null=True, blank=True)
    konNoKPPengurus = models.CharField(max_length=20, null=True, blank=True)
    konNoTelPengurus = models.CharField(max_length=20, null=True, blank=True)
    #maklumat rakan konsi
    konRKsatu = models.CharField(max_length=150, null=True, blank=True)
    konRKsatuNokp = models.CharField(max_length=20, null=True, blank=True)
    konRKsatuNoTel = models.CharField(max_length=20, null=True, blank=True)
    konRKdua = models.CharField(max_length=150, null=True, blank=True)
    konRKduaNokp = models.CharField(max_length=20, null=True, blank=True)
    konRKduaNoTel = models.CharField(max_length=20, null=True, blank=True)
    konRKtiga = models.CharField(max_length=150, null=True, blank=True)
    konRKtigaNokp = models.CharField(max_length=20, null=True, blank=True)
    konRKtigaNoTel = models.CharField(max_length=20, null=True, blank=True)
    konRKempat = models.CharField(max_length=150, null=True, blank=True)
    konRKempatNokp = models.CharField(max_length=20, null=True, blank=True)
    konRKempatNoTel = models.CharField(max_length=20, null=True, blank=True)
    #Jenis Permohonan
    konJPBaru = models.CharField(max_length=150, null=True, blank=True)
    konJPPembaharuan = models.CharField(max_length=20, null=True, blank=True)
    konJPLainLain = models.CharField(max_length=20, null=True, blank=True)
    konJPKategori = models.CharField(max_length=20, null=True, blank=True)
    #malumat Permohonan]
    konMPTarikhMohon = models.CharField(max_length=20, null=True, blank=True)
    konMPCas = models.CharField(max_length=200, null=True, blank=True)
    konMPNoResit = models.CharField(max_length=150, null=True, blank=True) 
    konMPNoSijil = models.CharField(max_length=50, null=True, blank=True)
    konMPtarikhkeluar = models.CharField(max_length=50, null=True, blank=True) 
    konMPtarikhtamat = models.CharField(max_length=50, null=True, blank=True)
    #Disemak
    konMPdisemak = models.CharField(max_length=50, null=True, blank=True)
    konMPjawatansemak = models.CharField(max_length=50, null=True, blank=True)
    konMPdisah = models.CharField(max_length=50, null=True, blank=True)
    konMPjawatansah  = models.CharField(max_length=50, null=True, blank=True)
    konMPlulus= models.CharField(max_length=50, null=True, blank=True)
    konMPjawatanlulus = models.CharField(max_length=50, null=True, blank=True)
    #sijil Perakuan pendaftaran kontraktor (PPK)
    sijilPPKNoPendaftaran = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKSahDari = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKTamat  = models.CharField(max_length=50, null=True, blank=True)  
    sijilPPKGredSatu = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKKatSatu = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKKhuSatu = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKGredDua = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKKatDua = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKKhuDua = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKGredTiga = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKKatTiga = models.CharField(max_length=50, null=True, blank=True)
    sijilPPKKhuTiga = models.CharField(max_length=50, null=True, blank=True)
    #sijil Perakuan pendaftaran kontraktor (SPKK)
    sijilSPKKNoPendaftaran = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKSahDari = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKTamat = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKGredSatu = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKKatSatu = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKKhuSatu = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKGredDua = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKKatDua = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKKhuDua = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKGredTiga = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKKatTiga = models.CharField(max_length=50, null=True, blank=True)
    sijilSPKKKhuTiga = models.CharField(max_length=50, null=True, blank=True)
    #sijilTarahBumiputera
    sijilSTBNoPendaftaran = models.CharField(max_length=50, null=True, blank=True)
    sijilSTBSahDari = models.CharField(max_length=50, null=True, blank=True)
    sijilSTBTamat = models.CharField(max_length=50, null=True, blank=True)
    sijilSTBGred = models.CharField(max_length=50, null=True, blank=True)
    #sijilSSM
    sijilSSMNoPendaftaran = models.CharField(max_length=50, null=True, blank=True)
    sijilSSMSahDari = models.CharField(max_length=50, null=True, blank=True)
    sijilSSMTamat = models.CharField(max_length=50, null=True, blank=True)
    #sijilSST
    sijilSSTNoPendaftaran = models.CharField(max_length=50, null=True, blank=True)
    sijilSSTSahDari = models.CharField(max_length=50, null=True, blank=True)
    sijilSSTTamat = models.CharField(max_length=50, null=True, blank=True)
    #sijilJPS
    sijilJPSNoPendaftaran = models.CharField(max_length=50, null=True, blank=True)
    sijilJPSSahDari = models.CharField(max_length=50, null=True, blank=True)
    sijilJPSTamat = models.CharField(max_length=50, null=True, blank=True) 
    sijilJPSGred = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.konNama



class Projek:
    pass

class Order(models.Model):
    o_sebutharga  = models.CharField(max_length=150, null=True, blank=True)
    o_tarikh  = models.CharField(max_length=50, null=True, blank=True)
    o_permilik  = models.CharField(max_length=150, null=True, blank=True)
    o_jenis = models.CharField(max_length=50, null=True, blank=True)

class MR1:
    pass

class MR2:
    pass

class MR3:
    pass
