from django import forms
from ..modelcontroller import dfnoperolehan, userprofile, project
from django.contrib.auth.models import User


class Projekform(forms.ModelForm):


    daerah = (
        ('Tiada','Tiada'),
        ('Kuala Muda','Kuala Muda'),
        ('Sik','Sik'),
        ('Baling','Baling'),
    )

    gred = (
    
        ('Tiada','Tiada'),
        ('G1','G1'),
        ('G2','G2'),
        ('G3','G3'),
        ('G4','G4'),
        ('G5','G5'),
        ('G6','G6'),
        ('G7','G7')   
    )

    catkontraktor = (
    
        ('Tiada','Tiada'),
        ('B','B'),
        ('CE','CE'),
        ('ME','ME'), 
    )


    taraf = (
    
        ('Tiada','Tiada'),
        ('Bumiputera','Bumiputera'),
        ('Bukan Bumiputera','Bukan Bumiputera'),
    )

    tempoh = (
    
        ('Tiada','Tiada'),
        ('Minggu','Minggu'),
        ('Bulan','Bulan'),
    )

    peruntutkan = (
    
        ('Tiada','Tiada'),
        ('Negeri','Negeri'),
        ('Perseketuan','Perseketuan'),
    )


    tajukkerja = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','type':'text','placeholder':'Tajuk Kerja','rows':'5'}))
    daerah = forms.ChoiceField(choices=daerah, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    pgred = forms.ChoiceField(choices=gred, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    pkategori = forms.ChoiceField(choices=catkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    pkhususan1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    pkhususan2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    pkhususan3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    ptaraf = forms.ChoiceField(choices=taraf, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    ptempohsiap = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    pweekormonth = forms.ChoiceField(choices=tempoh, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    hargadukumen = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    tarikhnotis = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker2','placeholder':'MM/DD/YYYY'}))
    tariklawattapak = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    tarikhdukemenjual = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    tarikhakhirdukemenjual = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    tarikhtutupsebutharga =forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    pjuruteradearah = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    pjurutera = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    pjuruterakanan36 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    pjurutera29 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    kodvot = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    peruntukan = forms.ChoiceField(choices=peruntutkan, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    peruntukansemasa =forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    latitud1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    latitud2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    latitud3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    longlitud1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    longlitud2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    longlitud3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    lembangansungai = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    sistem = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    subsistem = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    komponen = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    dimensi = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))
    nosebuthargaid = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':''}))  
  


    class Meta:
        model = project.Projek
        fields = [
            'tajukkerja',
            'daerah',
            'pgred', 
            'pkategori', 
            'pkhususan1', 
            'pkhususan2',
            'pkhususan3', 
            'ptaraf', 
            'ptempohsiap', 
            'pweekormonth', 
            'hargadukumen', 
            'tarikhnotis', 
            'tariklawattapak', 
            'tarikhdukemenjual',
            'tarikhakhirdukemenjual',
            'tarikhtutupsebutharga',
            'pjuruteradearah', 
            'pjurutera',
            'pjuruterakanan36',
            'pjurutera29', 
            'kodvot', 
            'peruntukan', 
            'peruntukansemasa', 
            'latitud1',
            'latitud2', 
            'latitud3', 
            'longlitud1', 
            'longlitud2',
            'longlitud3', 
            'lembangansungai', 
            'sistem', 
            'subsistem', 
            'komponen', 
            'dimensi', 
            'nosebuthargaid',
        ]