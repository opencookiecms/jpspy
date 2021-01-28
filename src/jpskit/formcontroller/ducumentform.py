from django import forms
from ..modelcontroller import dfnoperolehan, kontraktor,document
from django.contrib.auth.models import User


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


    mrksatunoinden = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrksatugred = forms.ChoiceField(choices=gred, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    mrksatukategori  = forms.ChoiceField(choices=kategori, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    mrksatupengkhususan = forms.ChoiceField(choices="", required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    mrksatutarikhmula = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrksatutarikhjangkasiap = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))

    mrksatukosprojek = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'RM 100,000.00'}))
    mrksatutarikhdaftar = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrksatunosebutharga = forms.ModelChoiceField(required=False, queryset=dfnoperolehan.NoPerolehan.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select29'}))
    mrksatukontraktor = forms.ModelChoiceField(required=False, queryset=kontraktor.Kontraktor.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select29'}))


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
            'mrksatunosebutharga',
            'mrksatukontraktor'

        ]


class MRKDuaForm(forms.ModelForm):


    mrkduakerjajadual  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduakerjasebenartarikh = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduakerjasebenar = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduakemajuan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduabayarankemajuan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduamodal = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mkrduabahan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduapekerja = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduatapak = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduacuaca = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduadisebabkan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkdualainlain = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkdualanjutmasa = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkdualanjutdari = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkdualanjutsehingga = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduadisebabkan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduaLAD = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Inden'}))
    mrkduaLADdari = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduaLADSehingga = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduaperakuan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduamansuh = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduatarikhlaporan  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    mrkduanosebutharga  = forms.ModelChoiceField(required=False, queryset=dfnoperolehan.NoPerolehan.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select29'}))
    mrksatulink  = forms.ModelChoiceField(required=False, queryset=document.MRKSatu.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select29'}))


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
            'mrkduadisebabkan',
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
            'mrkduanosebutharga',
            'mrksatulink'
        ]
   