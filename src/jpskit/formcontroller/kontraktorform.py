from django import forms
from datacontroller import kontraktor

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

        daerah = (
            
            ('Tiada','Tiada'),
            ('Kuala Muda','Kuala Muda'),
            ('Sik','Sik'),
            ('Baling','Baling'),
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
        gredkontraktor = (
    
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

        stbgred = (
    
            ('Tiada','Tiada'),
            ('Kontraktor','Kontraktor'),
            ('Pembekal','Pembekal'),

        )

        jawatan = (
    
            ('Tiada','Tiada'),
            ('Jurutera','Jurutera'),
            ('Penolong Jurutera','Penolong Jurutera'),
            ('Jurutera Dearah','Jurutera Dearah'), 
            ('Pembantu Tadbir Kanan','Pembantu Tadbir Kanan'), 
        )

        konNama = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cht:Syarikat ABC'}))
        konImage = forms.FileField(required=False)
        konAlamat = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:N0 1821 Lorong Peruda 1'}))
        konAlamatExtS = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Taman Peruda'}) )
        konAlamatExtD = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Bakar Arang'}) )
        konPoskod = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'eg:08000'}) )
        konBandar = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg:Sungai Petani'}) )
        konDaerah = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg:Kuala Muda'}) )
        konNegeri = forms.ChoiceField(choices=negeri, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select2','placholder':'negeri'}))
        konTel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'04-XXXXXXX"'}) )
        konEmail = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:adk@gmail.com'}))
        konFax = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:010-1234567'}) )
        konBank = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Maybank, RHB Bank, CIMB Bank'}) )
        konNoAkaun = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'No akaun bank terkini'}) )
        konKawOperasi = forms.ChoiceField(choices=operasi, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select21','placholder':'kawasan operasi'}))
        konPrestasi = forms.ChoiceField(choices=prestasi, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select22','placholder':'prestasi'}))
        #maklumat pengurus
        konPengurus = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg:Ahmad bin Hassan'}))
        konNoKPPengurus = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg:72XXXX-00-XXXX'}) )
        konNoTelPengurus = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:010-1234567'}) )
        #maklumat rakan konsi
        konRKsatu = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Salah'}))
        konRKsatuNokp = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:83XXXX-XX-XXXX'}) )
        konRKsatuNoTel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:012-12334456'}) )

        konRKdua = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Salah'}))
        konRKduaNokp = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:83XXXX-XX-XXXX'}) )
        konRKduaNoTel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:012-12334456'}) )

        konRKtiga = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Salah'}))
        konRKtigaNokp = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:83XXXX-XX-XXXX'}) )
        konRKtigaNoTel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:012-12334456'}) )

        konRKempat = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:Salah'}))
        konRKempatNokp = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:83XXXX-XX-XXXX'}))
        konRKempatNoTel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:012-12334456'}))
        #Jenis Permohonan
        konJPBaru = forms.ChoiceField(choices=yesorno, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select23 ','placholder':'baru'}))
        konJPPembaharuan = forms.ChoiceField(choices=yesorno, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select24','placholder':'baru'}))
        konJPLainLain = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'lain-lain'}))
        konJPKategori = forms.ChoiceField(choices=katergorikontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select25','placholder':'baru'}))
        #malumat Permohonan]
        konMPTarikhMohon = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        konMPCas = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'10.00'}))
        konMPNoResit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:JPS-2938HS'})) 
        konMPNoSijil = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'JPS0293us932'}))
        konMPtarikhkeluar = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'})) 
        konMPtarikhtamat = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        #Disemak
        
        konMPdisemak = forms.ModelChoiceField(required=False, queryset=UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select26'}))
        konMPjawatansemak = forms.ChoiceField(choices=jawatan, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select26 ','placholder':'baru'}))
        konMPdisah = forms.ModelChoiceField(required=False, queryset=UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select26'}))
        konMPjawatansah  = forms.ChoiceField(choices=jawatan, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select26 ','placholder':'baru'}))
        konMPlulus = forms.ModelChoiceField(required=False, queryset=UserProfile.objects.all(), widget=forms.Select(attrs={'class':'form-control custom-select select26'}))
        konMPjawatanlulus = forms.ChoiceField(choices=jawatan, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select26 ','placholder':'baru'}))
        #sijil Perakuan pendaftaran kontraktor (PPK)
        sijilPPKNoPendaftaran = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilPPKSahDari = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        sijilPPKTamat  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))  
        sijilPPKGredSatu = forms.ChoiceField(choices=gredkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilPPKKatSatu = forms.ChoiceField(choices=catkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilPPKKhuSatu = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:G1, G5, B, CE'}) )
        sijilPPKGredDua = forms.ChoiceField(choices=gredkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilPPKKatDua = forms.ChoiceField(choices=catkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilPPKKhuDua = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:G1, G5, B, CE'}) )
        sijilPPKGredTiga = forms.ChoiceField(choices=gredkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilPPKKatTiga = forms.ChoiceField(choices=catkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilPPKKhuTiga = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:G1, G5, B, CE'}) )
        #sijil Perakuan pendaftaran kontraktor (SPKK)
        sijilSPKKNoPendaftaran = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSPKKSahDari = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        sijilSPKKTamat = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        sijilSPKKGredSatu = forms.ChoiceField(choices=gredkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilSPKKKatSatu = forms.ChoiceField(choices=catkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilSPKKKhuSatu = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:G1, G5, B, CE'}) )
        sijilSPKKGredDua = forms.ChoiceField(choices=gredkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilSPKKKatDua = forms.ChoiceField(choices=catkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilSPKKKhuDua = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:G1, G5, B, CE'}) )
        sijilSPKKGredTiga = forms.ChoiceField(choices=gredkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilSPKKKatTiga = forms.ChoiceField(choices=catkontraktor, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        sijilSPKKKhuTiga = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'cth:G1, G5, B, CE'}) )
        #sijilTarahBumiputera
        sijilSTBNoPendaftaran = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSTBSahDari =forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        sijilSTBTamat = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        sijilSTBGred = forms.ChoiceField(choices=stbgred, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))
        #sijilSSM
        sijilSSMNoPendaftaran = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilSSMSahDari = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        sijilSSMTamat = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        #sijilSST
        sijilSSTNoPendaftaran = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}))
        sijilSSTSahDari = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        sijilSSTTamat = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        #sijilJPS
        sijilJPSNoPendaftaran = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'none'}) )
        sijilJPSSahDari = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        sijilJPSTamat = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control fc-datepicker','placeholder':'MM/DD/YYYY'}))
        sijilJPSGred = forms.ChoiceField(choices=stbgred, required=False, widget=forms.Select(attrs={'class':'form-control custom-select select27 ','placholder':'baru'}))


        class Meta:
            model = kontraktor.Kontraktor
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