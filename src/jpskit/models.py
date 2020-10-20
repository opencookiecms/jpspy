from django.db import models

# Create your models here.
class Kontraktor(models.Model):
    
    #maklumat syarikat
    konNama = models.CharField(max_length=100, blank=True)
    konImage = models.CharField(max_length=150, blank=True)
    konAlamat = models.CharField(max_length=200, blank=True)
    konAlamatExtS = models.CharField(max_length=50, blank=True)
    konAlamatExtD = models.CharField(max_length=20, blank=True)
    konPoskod = models.CharField(max_length=10, blank=True)
    konBandar = models.CharField(max_length=20, blank=True)
    konDaerah = models.CharField(max_length=20, blank=True)
    konNegeri = models.CharField(max_length=20, blank=True)
    konTel = models.CharField(max_length=20, blank=True)
    konEmail = models.CharField(max_length=150, blank=True)
    konFax = models.CharField(max_length=20, blank=True)
    konBank = models.CharField(max_length=50, blank=True)
    konNoAkaun = models.CharField(max_length=50, blank=True)
    konKawOperasi = models.CharField(max_length=20, blank=True)
    konPrestasi = models.CharField(max_length=10, blank=True)
    #maklumat pengurus
    konPengurus = models.CharField(max_length=150, blank=True)
    konNoKPPengurus = models.CharField(max_length=20, blank=True)
    konNoTelPengurus = models.CharField(max_length=20, blank=True)
    #maklumat rakan konsi
    konRKsatu = models.CharField(max_length=150, blank=True)
    konRKsatuNokp = models.CharField(max_length=20, blank=True)
    konRKsatuNoTel = models.CharField(max_length=20, blank=True)
    konRKdua = models.CharField(max_length=150, blank=True)
    konRKduaNokp = models.CharField(max_length=20, blank=True)
    konRKduaNoTel = models.CharField(max_length=20, blank=True)
    konRKtiga = models.CharField(max_length=150, blank=True)
    konRKtigaNokp = models.CharField(max_length=20, blank=True)
    konRKtigaNoTel = models.CharField(max_length=20, blank=True)
    konRKempat = models.CharField(max_length=150, blank=True)
    konRKempatNokp = models.CharField(max_length=20, blank=True)
    konRKempatNoTel = models.CharField(max_length=20, blank=True)
    #Jenis Permohonan
    konJPBaru = models.CharField(max_length=150, blank=True)
    konJPPembaharuan = models.CharField(max_length=20, blank=True)
    konJPLainLain = models.CharField(max_length=20, blank=True)
    konJPKategori = models.CharField(max_length=20, blank=True)
    #malumat Permohonan]
    konMPTarikhMohon = models.CharField(max_length=20, blank=True)
    konMPCas = models.CharField(max_length=200, blank=True)
    konMPNoResit = models.CharField(max_length=150, blank=True) 
    konMPNoSijil = models.CharField(max_length=50, blank=True)
    konMPtarikhkeluar = models.CharField(max_length=50, blank=True) 
    konMPtarikhtamat = models.CharField(max_length=50, blank=True)
    #Disemak
    konMPdisemak = models.CharField(max_length=50, blank=True)
    konMPjawatansemak = models.CharField(max_length=50, blank=True)
    konMPdisah = models.CharField(max_length=50, blank=True)
    konMPjawatansah  = models.CharField(max_length=50, blank=True)
    konMPlulus= models.CharField(max_length=50, blank=True)
    konMPjawatanlulus = models.CharField(max_length=50, blank=True)
    #sijil Perakuan pendaftaran kontraktor (PPK)
    sijilPPKNoPendaftaran = models.CharField(max_length=50, blank=True)
    sijilPPKSahDari = models.CharField(max_length=50, blank=True)
    sijilPPKTamat  = models.CharField(max_length=50, blank=True)  
    sijilPPKGredSatu = models.CharField(max_length=50, blank=True)
    sijilPPKKatSatu = models.CharField(max_length=50, blank=True)
    sijilPPKKhuSatu = models.CharField(max_length=50, blank=True)
    sijilPPKGredDua = models.CharField(max_length=50, blank=True)
    sijilPPKKatDua = models.CharField(max_length=50, blank=True)
    sijilPPKKhuDua = models.CharField(max_length=50, blank=True)
    sijilPPKGredTiga = models.CharField(max_length=50, blank=True)
    sijilPPKKatTiga = models.CharField(max_length=50, blank=True)
    sijilPPKKhuTiga = models.CharField(max_length=50, blank=True)
    #sijil Perakuan pendaftaran kontraktor (SPKK)
    sijilSPKKNoPendaftaran = models.CharField(max_length=50, blank=True)
    sijilSPKKSahDari = models.CharField(max_length=50, blank=True)
    sijilSPKKTamat = models.CharField(max_length=50, blank=True)
    sijilSPKKGredSatu = models.CharField(max_length=50, blank=True)
    sijilSPKKKatSatu = models.CharField(max_length=50, blank=True)
    sijilSPKKKhuSatu = models.CharField(max_length=50, blank=True)
    sijilSPKKGredDua = models.CharField(max_length=50, blank=True)
    sijilSPKKKatDua = models.CharField(max_length=50, blank=True)
    sijilSPKKKhuDua = models.CharField(max_length=50, blank=True)
    sijilSPKKGredTiga = models.CharField(max_length=50, blank=True)
    sijilSPKKKatTiga = models.CharField(max_length=50, blank=True)
    sijilSPKKKhuTiga = models.CharField(max_length=50, blank=True)
    #sijilTarahBumiputera
    sijilSTBNoPendaftaran = models.CharField(max_length=50, blank=True)
    sijilSTBSahDari = models.CharField(max_length=50, blank=True)
    sijilSTBTamat = models.CharField(max_length=50, blank=True)
    sijilSTBGred = models.CharField(max_length=50, blank=True)
    #sijilSSM
    sijilSSMNoPendaftaran = models.CharField(max_length=50, blank=True)
    sijilSSMSahDari = models.CharField(max_length=50, blank=True)
    sijilSSMTamat = models.CharField(max_length=50, blank=True)
    #sijilSST
    sijilSSTNoPendaftaran = models.CharField(max_length=50, blank=True)
    sijilSSTSahDari = models.CharField(max_length=50, blank=True)
    sijilSSTTamat = models.CharField(max_length=50, blank=True)
    #sijilJPS
    sijilJPSNoPendaftaran = models.CharField(max_length=50, blank=True)
    sijilJPSSahDari = models.CharField(max_length=50, blank=True)
    sijilJPSTamat = models.CharField(max_length=50, blank=True) 
    sijilJPSGred = models.CharField(max_length=50, blank=True)


class Projek:
    pass

class MR1:
    pass

class MR2:
    pass

class MR3:
    pass
