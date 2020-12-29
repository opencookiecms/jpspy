from django import forms
from ..modelcontroller import dnoperolehan, userprofile

class DPerolehanForm(forms.ModelForm):

    kaedah = (
    
        ('Tiada','Tiada'),
        ('Lantikan Terus','Lantikan Terus'),
        ('Sebutharga','Sebutharga'),
        ('Undi','Undi')

    )

    noperolehan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','type':'text','value':'hale'}))
    tarikh  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
    kaedahperolehan  = forms.ChoiceField(choices=kaedah, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select28 ','placholder':'baru'}))
    pegawaiselia  = forms.ModelChoiceField(required=False, queryset= userprofile.UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select29'}))

    class Meta:
        model = dnoperolehan.NoPerolehan
        fields = [
            'noperolehan',
            'tarikh',
            'kaedahperolehan',
            'pegawaiselia'
        ]