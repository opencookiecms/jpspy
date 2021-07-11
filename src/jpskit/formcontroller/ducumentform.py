from django import forms
from ..modelcontroller import dfnoperolehan, kontraktor,document,project
from django.contrib.auth.models import User
from django.conf import settings


class MRK1Form(forms.ModelForm):

    gred = (
    
        ('Tiada','Tiada'),
        ('G1','G1 | Sehingga RM200,000.00'),
        ('G2','G2 | RM200,001.00 Hingga RM500,000.00'),
        ('G3','G3 | RM500,001.00 Hingga RM1 000,000.00'),
        ('G4','G4 | RM1 000,001.00 Hingga RM3 000,000.00'),
        ('G5','G5 | RM300,001.00 Hingga RM5 000,000.00'),
        ('G6','G6 | RM5 000,001.00 Hingga RM10 000,000.00'),
        ('G7','G7 | RM 10 000,001.00 Ke Atas')   
    )

    kategori = (
        ('Tiada','Tiada'),
        ('CE','CE | Pembinaan Kejuruteraan Awam'),
        ('B','B | Pembinaan Bangunan'),
        ('ME','ME | Mekanikal & Elektrikal'),

    )


    mrksatunoinden = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'No Inden'}))
    mrksatugred = forms.ChoiceField(choices=gred, required=False, widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 font-size-18 custom-select select28 ','placholder':'baru'}))
    mrksatukategori  = forms.ChoiceField(choices=kategori, required=False, widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 font-size-18 custom-select select28 ','placholder':'baru'}))
    mrksatupengkhususan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'No Inden'}))
    mrksatutarikhmula = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrksatutarikhjangkasiap = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False, widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrksatukosprojek = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'RM 100,000.00'}))
    mrksatutarikhdaftar = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    projekbind = forms.ModelChoiceField(required=False, queryset=project.Projek.objects.all(), widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select29'}))
    mrksatukontraktor = forms.ModelChoiceField(required=False, queryset=kontraktor.Kontraktor.objects.all(), widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select29'}))


    class Meta:
        model = document.MRKSatu
        fields = [
            'mrksatunoinden',
            'mrksatugred',
            'mrksatukategori',
            'mrksatupengkhususan',
            'mrksatutarikhmula',
            'mrksatutarikhjangkasiap',
            'mrksatukosprojek',
            'mrksatutarikhdaftar',
            'mrksatukontraktor',
            'projekbind',
          

        ]


class MRKDuaForm(forms.ModelForm):


    mrkduakerjajadual  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Kemajuan Kerja '}))
    mrkduakerjasebenartarikh = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduakerjasebenar = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Kerja Sebenar'}))
    mrkduakemajuan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Kemajuan Semasa'}))
    mrkduabayarankemajuan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600 ml-10','type':'text','placeholder':'0.00'}))


    mrkduadisebabkanoleh = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Disebabkan oleh','rows':'2'}))
    mrkdualainlain = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Lain-lain','rows':'2'}))
    mrkdualanjutmasa = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Masa/Hari'}))
    mrkdualanjutdari = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkdualanjutsehingga = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduadisebabkan = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Disebabkan','rows':'2'}))
    mrkduaLAD = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600 ml-10','type':'text','placeholder':'0.00'}))
    mrkduaLADdari = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduaLADSehingga = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduaperakuan = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduamansuh = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduatarikhlaporan  = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    projekbind  = forms.ModelChoiceField(required=False, queryset=project.Projek.objects.all(), widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select29'}))
    mrksatulink  = forms.ModelChoiceField(required=False, queryset=document.MRKSatu.objects.all(), widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select29'}))


    class Meta:
        model = document.MRKDua

        fields = [
            'mrkduakerjajadual',
            'mrkduakerjasebenartarikh',
            'mrkduakerjasebenar',
            'mrkduakemajuan',
            'mrkduabayarankemajuan',
            'mrkduamodal',
            'mkrduabahan',
            'mrkduapekerja',
            'mrkduatapak',
            'mrkduacuaca',
            'mrkduadisebabkanoleh',
            'mrkdualainlain',
            'mrkdualanjutmasa',
            'mrkdualanjutdari',
            'mrkdualanjutsehingga',
            'mrkduadisebabkan',
            'mrkduaLAD',
            'mrkduaLADdari',
            'mrkduaLADSehingga',
            'mrkduaperakuan',
            'mrkduamansuh',
            'mrkduatarikhlaporan',
            'projekbind',
            'mrksatulink'
        ]

class LSKForm(forms.ModelForm):

    ins = (
        ('Tiada','Tiada'),
        ('PL','PL | Public Liability'),
        ('AR','AR | All Risk'),
        ('IK','IK | Insurans Kerja'),

    )

    lskhargasebenar = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    lsklanjutmasa = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    lskkerjasiap = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    lskperuntukan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'contoh:- B13-28209'}))
    lsklaporan = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Laporan Kerja','rows':'5'}))
    lsktarikhperakui = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))

    lskketuabahagian = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    lskjawatanketuabahagian = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    lskjuruteraj41 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    lskjawatanj41 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'})) 
    lskjuruteradaerah = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    lskjawatanjuruteradaerah = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))

    lskperkeso = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Perkeso'}))
    lskjenisinsurancesatu = forms.ChoiceField(choices=ins, required=False, widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select28 ','placholder':'baru'}))
    lsknoinsurancesatu = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'INS192773823'}))
    lskjenisinsurancedua =  forms.ChoiceField(choices=ins, required=False, widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select28 ','placholder':'baru'}))
    lsknoinsurancedua = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'INS287366223'}))


    class Meta:
        model = document.Laporansiapkerja
        fields = [
            'lskhargasebenar',
            'lsklanjutmasa',
            'lskkerjasiap',
            'lskperuntukan',
            'lsklaporan',
            'lsktarikhperakui',
            'lskketuabahagian',
            'lskjawatanketuabahagian',
            'lskjuruteraj41',
            'lskjawatanj41',
            'lskjuruteradaerah',
            'lskjawatanjuruteradaerah',
            'lskperkeso',
            'lskjenisinsurancesatu',
            'lsknoinsurancesatu',
            'lskjenisinsurancedua',
            'lsknoinsurancedua',
            'projekbind',
            'lskmrksatulink',
        ]


class MRKtigaForm(forms.ModelForm):


    mrkcatat1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'catatatan'}))
    mrkcatat2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'catatatan'}))
    mrkcatat3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'catatatan'}))
    mrkcatat4 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'catatatan'}))
    mrkcatat5 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'catatatan'}))
    mrkcatat6 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'catatatan'}))
    mrkcatat7 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'catatatan'}))
    mrkcatat8 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'catatatan'}))
    mrktigasokongan = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Tajuk Kerja','rows':'5'}))
    mrktigatarikh = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
 

    class Meta:
        model = document.MRKTiga
        fields = [
            'mrktigabina', 
            'mrktigatadbir',
            'mrktigakemajuan', 
            'mkrtigamutukerangka', 
            'mrktigamutukerja', 
            'mrktigamutukemasan', 
            'mrktigamutukerjaluar', 
            'mrktigapegawasan', 
            'mrkcatat1', 
            'mrkcatat2', 
            'mrkcatat3', 
            'mrkcatat4', 
            'mrkcatat5', 
            'mrkcatat6', 
            'mrkcatat7', 
            'mrkcatat8',
            'mrktigasokongan', 
            'mrktigatarikh', 
            'projekbind', 
            'marktigamrksatu',
        ]

class PSKForm(forms.ModelForm):

    psktarikhsiapsebenar = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    psktarikhambilmilik = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    psktarikhmulatanggug = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    psktarikhtamattanggung = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))


    class Meta:
        model = document.PSK
        fields = [
            'psktarikhsiapsebenar',
            'psktarikhambilmilik',
            'psktarikhmulatanggug',
            'psktarikhtamattanggung',
            'projekbind',
            'pskmrksatulink',
        ]


class SenaraiSemakanForm(forms.ModelForm):

    sstarikh = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))

    class Meta:
        model = document.SenaraiSemakan
        fields = [
            'ssinden', 
            'sslsk', 
            'ssti',
            'sssebutharga', 
            'sspt', 
            'ssjs',
            'sskts', 
            'ssds',
            'ssplm',
            'ssab', 
            'sscidb', 
            'sspkk', 
            'ssssm', 
            'sskk', 
            'ssinsurance',
            'ssgambar',
            'sstarikh',
            'projekbind', 
            'ssmrksatulink',
        ]

class Psmkform(forms.ModelForm):

    psmknojaminanbanka = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'No Kewangan Jaminan Bank/Insuran'}))
    psmkhargajaminana = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    psmkbakiwangjaminana = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    psmknojaminanbankab = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'No Kewangan Jaminan Bank/Insuran'}))
    psmkhargajaminanb = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    psmkbakiwangjaminanb = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    psmkkosbon = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    psmkbakikos = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))


    class Meta:
        model = document.PSMK
        fields = [

            'psmknojaminanbanka',
            'psmkhargajaminana',
            'psmkbakiwangjaminana',
            'psmknojaminanbankab',
            'psmkhargajaminanb',
            'psmkbakiwangjaminanb',
            'psmkkosbon',
            'psmkbakikos',
            'psmkpegawaipenguasa',
            'psmkjawatan',
            'projekbind',
            'psmkmrksatulink',

        ]

class JaminanBankForm(forms.ModelForm):

    rujukanbank  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Rujukan Bank'}))
    namabank = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'contoh:Bank Islam, Maybank'}))
    alamatbank  = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Alamat bank','rows':'5'}))
    alamatpemborongsurat  = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Alamat Pemborong','rows':'5'}))

    class Meta:
        model = document.SuratPJaminanbank
        fields = [
            'rujukanbank', 
            'namabank',
            'alamatbank', 
            'alamatpemborongsurat',
            'projekbind',
            'jbankmrksatulink',
        ]

class PwjpForm(forms.ModelForm):

    jawatan = (
        ('Penolong Jurutera JA29','Penolong Jurutera JA29'),
        ('Penolong Jurutera JA36','Penolong Jurutera JA36'),
        ('Jurutera ( Kuala Muda/Sik )','Jurutera ( Kuala Muda/Sik )'),
        ('urutera ( Baling )','urutera ( Baling )'),
        ('Jurutera Daerah<','Jurutera Daerah'),
        ('Penolong Jurutera JA38','Penolong Jurutera JA38'),
    )
    rujukantuan  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Rujukan Tuan'}))
    rujukankami = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Rujukan Kami'}))
    namarujukan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Akauntan Negara'}))
    alamatrujukan = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Alamat','rows':'5'}))
    koswjp = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    wjpjawatan = forms.ChoiceField(choices=jawatan, required=False, widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select28 ','placholder':'baru'}))

    


    class Meta:
        model = document.Perakuanpwjp
        fields = [
            'rujukantuan',
            'rujukankami',
            'namarujukan',
            'alamatrujukan', 
            'koswjp', 
            'wjppegawai', 
            'wjpjawatan',
            'projekbind',
            'wjpmrksatulink', 
        ]

class SuratMRKForm(forms.ModelForm):

    jawatan = (
        ('Tiada','Tiada'),
        ('Penolong Jurutera JA29','Penolong Jurutera JA29'),
        ('Penolong Jurutera JA36','Penolong Jurutera JA36'),
        ('Jurutera ( Kuala Muda/Sik )','Jurutera ( Kuala Muda/Sik )'),
        ('urutera ( Baling )','urutera ( Baling )'),
        ('Jurutera Daerah<','Jurutera Daerah'),
        ('Penolong Jurutera JA38','Penolong Jurutera JA38'),
    )

    jenisborang = (
        ('Tiada','Tiada'),
        ('MRK 01','MRK 01'),
        ('MRK 02','MRK 02'),
        ('MRK 03','MRK 03'),
    )

    smrkrujukantuan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Rujukan Tuan'}))
    smrktarikh  = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control text-dark font-weight-600 fc-datepicker','placeholder':'MM/DD/YYYY'}))
    smrkjenisborang  = forms.ChoiceField(choices=jenisborang, required=False, widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select28 ','placholder':'baru'}))
    smrknamarujukan  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Nama Rujukan'}))
    smkralamatrujukan  = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Alamat Rujukan','rows':'5'}))
    smrkjawatan = forms.ChoiceField(choices=jawatan, required=False, widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select28 ','placholder':'baru'}))


    class Meta:
        model = document.SuratMRK
        fields = [
            'smrkrujukantuan',
            'smrktarikh', 
            'smrkjenisborang', 
            'smrknamarujukan', 
            'smkralamatrujukan', 
            'smrkpegawai', 
            'smrkjawatan', 
            'projekbind', 
            'smrkmrksatulink', 
        ]


class SuratKhasForm(forms.ModelForm):

    jawatan = (
        ('Tiada','Tiada'),
        ('Penolong Jurutera JA29','Penolong Jurutera JA29'),
        ('Penolong Jurutera JA36','Penolong Jurutera JA36'),
        ('Jurutera ( Kuala Muda/Sik )','Jurutera ( Kuala Muda/Sik )'),
        ('urutera ( Baling )','urutera ( Baling )'),
        ('Jurutera Daerah<','Jurutera Daerah'),
        ('Penolong Jurutera JA38','Penolong Jurutera JA38'),
    )

    khasrujukantuan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Rujukan Tuan'}))
    khasnamarujukan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Rujukan Tuan'}))
    khasalamatrujukan = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Alamat Rujukan','rows':'5'}))
    khasjawatan = forms.ChoiceField(choices=jawatan, required=False, widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select28 ','placholder':'baru'}))

    class Meta:
        model = document.SuratKhas
        fields = [
            'khasrujukantuan', 
            'khasnamarujukan',
            'khasalamatrujukan', 
            'khaspegawai', 
            'khasjawatan',
            'projekbind',
            'khasmrksatulink', 
        ]

class SuratBonForm(forms.ModelForm):

    jawatan = (
        ('Tiada','Tiada'),
        ('Penolong Jurutera JA29','Penolong Jurutera JA29'),
        ('Penolong Jurutera JA36','Penolong Jurutera JA36'),
        ('Jurutera ( Kuala Muda/Sik )','Jurutera ( Kuala Muda/Sik )'),
        ('urutera ( Baling )','urutera ( Baling )'),
        ('Jurutera Daerah<','Jurutera Daerah'),
        ('Penolong Jurutera JA38','Penolong Jurutera JA38'),
    )

    bonkepada = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Rujukan Tuan'}))
    bonalamatsatu = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Alamat Rujukan','rows':'5'}))
    bonmelalui = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Melalui'}))
    bonalamatdua = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'Alamat Rujukan','rows':'5'}))
    bonwangjaminan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-dark font-weight-600','type':'text','placeholder':'0.00'}))
    bonjawatan = forms.ChoiceField(choices=jawatan, required=False, widget=forms.Select(attrs={'class':'form-control text-dark font-weight-600 custom-select select28 ','placholder':'baru'}))


    class Meta:
        model = document.SuratPelepasanBon
        fields = [
            'bonkepada', 
            'bonalamatsatu',
            'bonmelalui', 
            'bonalamatdua', 
            'bonwangjaminan', 
            'bonpegawai',
            'bonjawatan',
            'projekbind', 
            'bonmrksatulink',
        ]