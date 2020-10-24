from django import forms
from .models import Kontraktor

class KontraktroForm(forms.ModelForm):

        negeri = (
            ('Perlis','Perlis'),
            ('Kedah','Kedah'),
            ('P.Pinang','P.Pinang'),
            ('Kelantan','Kelantan'),
            ('Perak','Perak'),
            ('Pahang','Pahang'),
            ('Terengganu','Terengganu'),
            ('N.Sembilan','N.Sembilan'),
            ('Selangor','Selangor'),
            ('Kuala Lumpur','Kuala Lumpur'),
            ('Melaka','Melaka'),
            ('Johor','Johor'),
            ('Sabah','Sabah'),
            ('Sarawak','Sarawak'),
        )

        operasi = (
            ('Tiada','Tiada'),
            ('Kuala Muda','Kuala Muda'),
            ('Sik','Sik'),
            ('Baling','Baling'),
            ('Yan','Yan'),
            ('Kedah','Kedah'),
            ('Malaysia','Malaysia'),
        )

        prestasi = (
    
            ('Baik','Baik'),
            ('Cemerlang','Cemerlang'),
            ('Memuaskan','Memuaskan'),
            ('Sederhana','Sederhana'),
            ('Lemah','Lemah'),
            ('Tiada Rekod','Tiada Rekod'),
        )

        yesorno = (
    
            ('',''),
            ('Ya','Ya'),
            ('Tidak','Tidak'),
        )

        katergorikontraktor = (
    
            ('',''),
            ('Kontraktor','Kontraktor'),
            ('Pembekal','Pembekal'),
            ('Perkhidmatan','Perkhidmatan'),
            ('Pembekal/Kontraktor','Pembekal/Kontraktor'),
        )

        konNama = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cht:Syarikat ABC'}))
        konImage = forms.FileField()
        konAlamat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:N0 1821 Lorong Peruda 1'}))
        konAlamatExtS = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Taman Peruda'}) )
        konAlamatExtD = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Bakar Arang'}) )
        konPoskod = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'eg:08000'}) )
        konBandar = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg:Sungai Petani'}) )
        konDaerah = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg:Kuala Muda'}) )
        konNegeri = forms.ChoiceField(choices=negeri, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select2','placholder':'negeri'}))
        konTel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'04-XXXXXXX"'}) )
        konEmail = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:adk@gmail.com'}))
        konFax = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:010-1234567'}) )
        konBank = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Maybank, RHB Bank, CIMB Bank'}) )
        konNoAkaun = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'No akaun bank terkini'}) )
        konKawOperasi = forms.ChoiceField(choices=operasi, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select21','placholder':'kawasan operasi'}))
        konPrestasi = forms.ChoiceField(choices=prestasi, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select22','placholder':'prestasi'}))
        #maklumat pengurus
        konPengurus = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg:Ahmad bin Hassan'}))
        konNoKPPengurus = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg:72XXXX-00-XXXX'}) )
        konNoTelPengurus = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:010-1234567'}) )
        #maklumat rakan konsi
        konRKsatu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Salah'}))
        konRKsatuNokp = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:83XXXX-XX-XXXX'}) )
        konRKsatuNoTel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:012-12334456'}) )

        konRKdua = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Salah'}))
        konRKduaNokp = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:83XXXX-XX-XXXX'}) )
        konRKduaNoTel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:012-12334456'}) )

        konRKtiga = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Salah'}))
        konRKtigaNokp = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:83XXXX-XX-XXXX'}) )
        konRKtigaNoTel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:012-12334456'}) )

        konRKempat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Salah'}))
        konRKempatNokp = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:83XXXX-XX-XXXX'}))
        konRKempatNoTel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:012-12334456'}))
        #Jenis Permohonan
        konJPBaru = forms.ChoiceField(choices=yesorno, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select23 ','placholder':'baru'}))
        konJPPembaharuan = forms.ChoiceField(choices=yesorno, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select24','placholder':'baru'}))
        konJPLainLain = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'lain-lain'}))
        konJPKategori = forms.ChoiceField(choices=katergorikontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select25','placholder':'baru'}))
        #malumat Permohonan]
        konMPTarikhMohon = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'MM/DD/YYYY'}) )
        konMPCas = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'10.00'}))
        konMPNoResit = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:JPS-2938HS'})) 
        konMPNoSijil = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'JPS0293us932'}))
        konMPtarikhkeluar = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'MM/DD/YYYY'})) 
        konMPtarikhtamat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'MM/DD/YYYY'}))
        #Disemak
        konMPdisemak = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}))
        konMPjawatansemak = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}))
        konMPdisah = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}))
        konMPjawatansah  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        konMPlulus= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        konMPjawatanlulus = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        #sijil Perakuan pendaftaran kontraktor (PPK)
        sijilPPKNoPendaftaran = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKSahDari = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKTamat  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )  
        sijilPPKGredSatu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKKatSatu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKKhuSatu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKGredDua = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKKatDua = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKKhuDua = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKGredTiga = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKKatTiga = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKKhuTiga = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        #sijil Perakuan pendaftaran kontraktor (SPKK)
        sijilSPKKNoPendaftaran = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKSahDari = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKTamat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKGredSatu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKKatSatu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKKhuSatu = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKGredDua = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKKatDua = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKKhuDua = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKGredTiga = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKKatTiga = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKKhuTiga = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        #sijilTarahBumiputera
        sijilSTBNoPendaftaran = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSTBSahDari = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSTBTamat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSTBGred = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        #sijilSSM
        sijilSSMNoPendaftaran = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSSMSahDari = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSSMTamat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        #sijilSST
        sijilSSTNoPendaftaran = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSSTSahDari = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSSTTamat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        #sijilJPS
        sijilJPSNoPendaftaran = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilJPSSahDari = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilJPSTamat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) ) 
        sijilJPSGred = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )


        class Meta:
            model = Kontraktor
            fields = [
                'konNama',
                'konImage',
                'konAlamat', 
                'konAlamatExtS',
                'konAlamatExtD', 
                'konPoskod',
                'konBandar', 
                'konDaerah', 
                'konNegeri', 
                'konTel', 
                'konEmail', 
                'konFax',
                'konBank', 
                'konNoAkaun', 
                'konKawOperasi',
                'konPrestasi',
                 #maklumat pengurus
                'konPengurus', 
                'konNoKPPengurus', 
                'konNoTelPengurus', 
                #maklumat rakan konsi
                'konRKsatu', 
                'konRKsatuNokp',
                'konRKsatuNoTel', 
                'konRKdua', 
                'konRKduaNokp', 
                'konRKduaNoTel',
                'konRKtiga', 
                'konRKtigaNokp', 
                'konRKtigaNoTel', 
                'konRKempat', 
                'konRKempatNokp', 
                'konRKempatNoTel', 
                #Jenis Permohonan
                'konJPBaru', 
                'konJPPembaharuan', 
                'konJPLainLain', 
                'konJPKategori', 
                #malumat Permohonan]
                'konMPTarikhMohon',
                'konMPCas', 
                'konMPNoResit', 
                'konMPNoSijil', 
                'konMPtarikhkeluar', 
                'konMPtarikhtamat', 
                #Disemak
                'konMPdisemak', 
                'konMPjawatansemak', 
                'konMPdisah', 
                'konMPjawatansah',  
                'konMPlulus',
                'konMPjawatanlulus', 
                #sijil Perakuan pendaftaran kontraktor (PPK)
                'sijilPPKNoPendaftaran', 
                'sijilPPKSahDari', 
                'sijilPPKTamat',  
                'sijilPPKGredSatu', 
                'sijilPPKKatSatu', 
                'sijilPPKKhuSatu', 
                'sijilPPKGredDua', 
                'sijilPPKKatDua', 
                'sijilPPKKhuDua', 
                'sijilPPKGredTiga', 
                'sijilPPKKatTiga', 
                'sijilPPKKhuTiga', 
                #sijil Perakuan pendaftaran kontraktor (SPKK)
                'sijilSPKKNoPendaftaran', 
                'sijilSPKKSahDari', 
                'sijilSPKKTamat', 
                'sijilSPKKGredSatu', 
                'sijilSPKKKatSatu',
                'sijilSPKKKhuSatu', 
                'sijilSPKKGredDua', 
                'sijilSPKKKatDua',
                'sijilSPKKKhuDua', 
                'sijilSPKKGredTiga', 
                'sijilSPKKKatTiga',
                'sijilSPKKKhuTiga', 
                #sijilTarahBumiputera
                'sijilSTBNoPendaftaran', 
                'sijilSTBSahDari',
                'sijilSTBTamat',
                'sijilSTBGred',
                #sijilSSM
                'sijilSSMNoPendaftaran', 
                'sijilSSMSahDari',
                'sijilSSMTamat', 
                #sijilSST
                'sijilSSTNoPendaftaran', 
                'sijilSSTSahDari', 
                'sijilSSTTamat', 
                #sijilJPS
                'sijilJPSNoPendaftaran',
                'sijilJPSSahDari', 
                'sijilJPSTamat', 
                'sijilJPSGred'
            ]