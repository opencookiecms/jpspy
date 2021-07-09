from django import forms
from ..modelcontroller import kursus
from django.conf import settings


class Dkursusform(forms.ModelForm):

    tahun = (
        ('2022','2022'),
        ('2021','2021'),
        ('2020','2020'),
        ('2019','2019'),
        ('2018','2018'),

    )

    
    tajukkursus = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Tajuk Kursus'}))
    tarikhmula = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    tarikhakhir = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    tempat = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','type':'text','placeholder':'Tempat Kursus','rows':'5'}))
    tahun = forms.ChoiceField(choices=tahun, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    hari = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Tajuk Kursus'}))


    class Meta:
        model = kursus.Course
        fields = [
            'tajukkursus',
            'tarikhmula',
            'tarikhakhir',
            'tempat',
            'tahun',
            'hari',
        ]
    