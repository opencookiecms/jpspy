from django import forms
from ..modelcontroller import dfnoperolehan, userprofile
from django.contrib.auth.models import User
from django.conf import settings




class DPerolehanForm(forms.ModelForm):

    kaedah = (
    
        ('Tiada','Tiada'),
        ('Lantikan Terus','Lantikan Terus'),
        ('Sebutharga','Sebutharga'),
        ('Undi','Undi')

    )
    #"widget=forms.NumberInput
    noperolehan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'No Fail Sebutharga'}))
    tarikh  = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=forms.DateInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    kaedahperolehan  = forms.ChoiceField(choices=kaedah, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    pegawaiselia  = forms.ModelChoiceField(required=False, queryset=User.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select29'}))
    
    #pegawaiselia = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    

    class Meta:
        model = dfnoperolehan.NoPerolehan
        fields = [
            'noperolehan',
            'tarikh',
            'kaedahperolehan',
            'pegawaiselia'
        ]