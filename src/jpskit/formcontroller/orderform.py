from django import forms
from ..modelcontroller import order, userprofile

class OrderForm(forms.ModelForm):

    jenissebutharga = (
        ('Lantikan Terus','Lantikan Terus'),
        ('Sebutharga','Sebutharga'),
        ('Undi','Undi')
    )

    o_sebutharga  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:JPS-38iJeie9'}))
    o_tarikh  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':''}))
    o_permilik = forms.ModelChoiceField(required=False, queryset=userprofile.UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select26'}))
    o_jenis = forms.ChoiceField(choices=jenissebutharga, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select26 ','placholder':'baru'}))

    class Meta:
        model = order.Order
        fields = [
            'o_sebutharga',
            'o_tarikh',
            'o_permilik',
            'o_jenis'
        ]
