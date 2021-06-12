from django.db import models
from ..modelcontroller import document,dfnoperolehan,kontraktor,project
import uuid

class MRKKursus(models.Model):
    kscode = models.CharField(max_length=50, null=True, blank=True)
    ksname = models.CharField(max_length=100, null=True, blank=True)

class MRKSatu(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    mrksatunoinden = models.CharField(max_length=50, null=True, blank=True)
    mrksatugred = models.CharField(max_length=20, null=True, blank=True)
    mrksatukategori  = models.CharField(max_length=20, null=True, blank=True)
    mrksatupengkhususan = models.CharField(max_length=100, null=True, blank=True)
    mrksatutarikhmula =  models.DateField(null=True, blank=True)
    mrksatutarikhjangkasiap = models.DateField(null=True, blank=True)
    mrksatukosprojek = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    mrksatutarikhdaftar = models.DateField(null=True, blank=True)
    mrksatukontraktor = models.ForeignKey(kontraktor.Kontraktor, blank=True, null=True, on_delete = models.SET_NULL)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)

    
    class Meta: 
        # Add verbose name 
        verbose_name_plural = 'MRK 1'

class MRKDua(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    mrkduakerjajadual = models.CharField(max_length=50, null=True, blank=True)
    mrkduakerjasebenartarikh = models.DateField(null=True, blank=True)
    mrkduakerjasebenar = models.CharField(max_length=50, null=True, blank=True)
    mrkduakemajuan = models.CharField(max_length=50, null=True, blank=True)
    mrkduabayarankemajuan = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    mrkduamodal = models.CharField(max_length=50, null=True, blank=True)
    mkrduabahan = models.CharField(max_length=50, null=True, blank=True)
    mrkduapekerja = models.CharField(max_length=50, null=True, blank=True)
    mrkduatapak = models.CharField(max_length=50, null=True, blank=True)
    mrkduacuaca = models.CharField(max_length=50, null=True, blank=True)
    mrkduadisebabkanoleh = models.CharField(max_length=500, null=True, blank=True)
    mrkdualainlain = models.CharField(max_length=500, null=True, blank=True)
    mrkdualanjutmasa = models.CharField(max_length=50, null=True, blank=True)
    mrkdualanjutdari = models.DateField(null=True, blank=True)
    mrkdualanjutsehingga = models.DateField(null=True, blank=True)
    mrkduadisebabkan = models.CharField(max_length=500, null=True, blank=True)
    mrkduaLAD = models.CharField(max_length=50, null=True, blank=True)
    mrkduaLADdari = models.DateField(null=True, blank=True)
    mrkduaLADSehingga = models.DateField(null=True, blank=True)
    mrkduaperakuan = models.DateField(null=True, blank=True)
    mrkduamansuh = models.DateField(null=True, blank=True)
    mrkduatarikhlaporan = models.DateField(null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    mrksatulink = models.ForeignKey(MRKSatu, related_name="bindone", blank=True, null=True, on_delete = models.SET_NULL)

    class Meta: 
        # Add verbose name 
        verbose_name_plural = 'MRK 2'


class Laporansiapkerja(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    lskhargasebenar  = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    lsklanjutmasa  = models.DateField(null=True, blank=True)
    lskkerjasiap  = models.DateField(null=True, blank=True)
    lskperuntukan  = models.CharField(max_length=50, null=True, blank=True)
    lsklaporan  = models.CharField(max_length=500, null=True, blank=True)
    lsktarikhperakui  = models.DateField(null=True, blank=True)
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
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    lskmrksatulink  = models.ForeignKey(MRKSatu, related_name="bindtwo", blank=True, null=True, on_delete = models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Laporan Siap Kerja'


class MRKTiga(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    mrktigabina = models.CharField(max_length=50, null=True, blank=True)
    mrktigatadbir = models.CharField(max_length=50, null=True, blank=True)
    mrktigakemajuan = models.CharField(max_length=50, null=True, blank=True)
    mkrtigamutukerangka = models.CharField(max_length=50, null=True, blank=True)
    mrktigamutukerja = models.CharField(max_length=50, null=True, blank=True)
    mrktigamutukemasan = models.CharField(max_length=50, null=True, blank=True)
    mrktigamutukerjaluar = models.CharField(max_length=50, null=True, blank=True)
    mrktigapegawasan = models.CharField(max_length=50, null=True, blank=True)
    mrkcatat1 = models.CharField(max_length=150, null=True, blank=True)
    mrkcatat2 = models.CharField(max_length=150, null=True, blank=True)
    mrkcatat3 = models.CharField(max_length=150, null=True, blank=True)
    mrkcatat4 = models.CharField(max_length=150, null=True, blank=True)
    mrkcatat5 = models.CharField(max_length=150, null=True, blank=True)
    mrkcatat6 = models.CharField(max_length=150, null=True, blank=True)
    mrkcatat7 = models.CharField(max_length=150, null=True, blank=True)
    mrkcatat8 = models.CharField(max_length=150, null=True, blank=True)
    mrktigasokongan = models.CharField(max_length=500, null=True, blank=True)
    mrktigatarikh = models.DateField(null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    marktigamrksatu = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)

    class Meta:
        verbose_name_plural = 'MRK 3'

class PSK(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    psktarikhambilmilik = models.DateField(null=True, blank=True)
    psktarikhmulatanggug = models.DateField(null=True, blank=True)
    psktarikhtamattanggung = models.DateField(null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    pskmrksatulink = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)


    class Meta:
        verbose_name_plural = "Perakuan Siap Kerja"

class SenaraiSemakan(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    ssinden = models.CharField(max_length=10, null=True, blank=True)
    sslsk = models.CharField(max_length=10, null=True, blank=True)
    ssti = models.CharField(max_length=10, null=True, blank=True)
    sssebutharga = models.CharField(max_length=10, null=True, blank=True)
    sspt = models.CharField(max_length=10, null=True, blank=True)
    ssjs = models.CharField(max_length=10, null=True, blank=True)
    sskts = models.CharField(max_length=10, null=True, blank=True)
    ssds = models.CharField(max_length=10, null=True, blank=True)
    ssplm = models.CharField(max_length=10, null=True, blank=True)
    ssab = models.CharField(max_length=10, null=True, blank=True)
    sscidb = models.CharField(max_length=10, null=True, blank=True)
    sspkk = models.CharField(max_length=10, null=True, blank=True)
    ssssm = models.CharField(max_length=10, null=True, blank=True)
    sskk = models.CharField(max_length=10, null=True, blank=True)
    ssinsurance = models.CharField(max_length=10, null=True, blank=True)
    ssgambar = models.CharField(max_length=10, null=True, blank=True)
    sstarikh = models.DateField(null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    ssmrksatulink = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)

    class Meta:
        verbose_name_plural = "Senarai Semakan"

class PSMK(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    psmknojaminanbanka = models.CharField(max_length=50, null=True, blank=True)
    psmkhargajaminana = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    psmkbakiwangjaminana = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    psmknojaminanbankab = models.CharField(max_length=50, null=True, blank=True)
    psmkhargajaminanb = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    psmkbakiwangjaminanb = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    psmkkosbon = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    psmkbakikos = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    psmkpegawaipenguasa = models.CharField(max_length=50, null=True, blank=True)
    psmkjawatan = models.CharField(max_length=50, null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    psmkmrksatulink = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)

    class Meta:
        verbose_name_plural = "Perakuan Siap Membaiki Kecacatan"

class SuratPJaminanbank(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    rujukanbank  = models.CharField(max_length=50, null=True, blank=True)
    namabank = models.CharField(max_length=50, null=True, blank=True)
    alamatbank = models.CharField(max_length=200, null=True, blank=True)
    alamatpemborongsurat = models.CharField(max_length=200, null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    jbankmrksatulink = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)

    class Meta:
        verbose_name_plural = "Surat Pelepasan Jaminan Bank"

class Perakuanpwjp(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    rujukantuan = models.CharField(max_length=50, null=True, blank=True)
    rujukankami = models.CharField(max_length=50, null=True, blank=True)
    namarujukan = models.CharField(max_length=150, null=True, blank=True)
    alamatrujukan = models.CharField(max_length=200, null=True, blank=True)
    koswjp = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    wjppegawai = models.CharField(max_length=50, null=True, blank=True)
    wjpjawatan = models.CharField(max_length=50, null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    wjpmrksatulink = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)

     
    class Meta:
        verbose_name_plural = "PPWJP"

class SuratMRK(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    smrkrujukantuan  = models.CharField(max_length=50, null=True, blank=True)
    smrktarikh  = models.DateField(null=True, blank=True)
    smrkjenisborang  = models.CharField(max_length=50, null=True, blank=True)
    smrknamarujukan  = models.CharField(max_length=50, null=True, blank=True)
    smkralamatrujukan  = models.CharField(max_length=200, null=True, blank=True)
    smrkpegawai = models.CharField(max_length=50, null=True, blank=True)
    smrkjawatan = models.CharField(max_length=50, null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    smrkmrksatulink = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)

    class Meta:
        verbose_name_plural = "Surat MRK"

class SuratKhas(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    khasrujukantuan = models.CharField(max_length=50, null=True, blank=True)
    khasnamarujukan = models.CharField(max_length=50, null=True, blank=True)
    khasalamatrujukan = models.CharField(max_length=200, null=True, blank=True)
    khaspegawai = models.CharField(max_length=50, null=True, blank=True)
    khasjawatan = models.CharField(max_length=50, null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    khasmrksatulink = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)

    class Meta:
        verbose_name_plural = "Surat Khas"

class SuratPelepasanBon(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    bonkepada = models.CharField(max_length=150, null=True, blank=True)
    bonalamatsatu = models.CharField(max_length=200, null=True, blank=True)
    bonmelalui = models.CharField(max_length=150, null=True, blank=True)
    bonalamatdua = models.CharField(max_length=200, null=True, blank=True)
    bonwangjaminan = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    bonpegawai = models.CharField(max_length=50, null=True, blank=True)
    bonjawatan = models.CharField(max_length=50, null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
    bonmrksatulink = models.ForeignKey(MRKSatu, blank=True, null=True, on_delete = models.SET_NULL)

    class Meta:
        verbose_name_plural = "Surat Bon"


class kosprojek(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    kos_belanja = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    kos_tanggung = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    projekbind = models.ForeignKey(project.Projek, blank=True, null=True, on_delete = models.SET_NULL)
 
















