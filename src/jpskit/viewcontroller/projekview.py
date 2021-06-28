from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import project,dfnoperolehan,document
from ..formcontroller import projekform
from django.db.models import Q
from django.db.models import Count
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def daftarprojek(request):
    
    form = projekform.Projekform(request.POST or None)
    if form.is_valid():
        form.save()
        form = projekform.Projekform()
        return redirect('projek/maklumatperolehan')  
        
    else:
        print("no data was post yet")
        print (form.errors)

    
    context = {
        'form':form,
        'sungai':project.isSungai.objects.all(),
        'sebutharga': dfnoperolehan.NoPerolehan.objects.all(),
    }

    return render(request, 'pages/projek-daftar.html',context)



@login_required(login_url='login')
def maklumatperolehan(request):


    p = project.Projek.objects.all().exists()

    if p:

        data = {
            'titleboard':'Projek Dashboard',
            'isexist':p,
            'senaraiprojek':project.Projek.objects.all(),
            'totalprojek':project.Projek.objects.all().count(),
            'kodvod':project.Projek.objects.values('kodvot').annotate(jumlah=Count('kodvot')),
            'total':project.Projek.objects.aggregate(
                sebutharga = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan='Sebutharga')),
                undi = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan='Undi')),
                lantikan = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan='Lantikan Terus')),
            ), 
        }
    else:
        
        data = {
            'titleboard':'Projek Dashboard',
            'isexist':p
        }



    return render(request, 'pages/maklumatperolehandash.html',data)


@login_required(login_url='login')
def maklumatperolehanjenis(request, jenisp):

    p = project.Projek.objects.all().exists()

    if p:

        data = {
            'titleboard':'Projek Dashboard',
            'isexist':p,
            'senaraiprojek':project.Projek.objects.filter(nosebuthargaid__kaedahperolehan=jenisp).annotate(total=Count('kodvot')),
            'kodvod':project.Projek.objects.filter(nosebuthargaid__kaedahperolehan=jenisp).annotate(jumlah=Count('kodvot')),
            'totalprojek':project.Projek.objects.all().count(),
            'total':project.Projek.objects.aggregate(
                sebutharga = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan="Sebutharga")),
                undi = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan="Undi")),
                lantikan = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan="Lantikan Terus")),
            ),
        }
    else:
        data = {
            'titleboard':'Projek Dashboard',
            'isexist':p
        }

    return render(request, 'pages/maklumatperolehandash.html',data)


@login_required(login_url='login')
def senaraiprojek(request):

    data = {
        'senaraiprojek':project.Projek.objects.all()
    }

    return render(request, 'pages/projek-senarai.html',data)


@login_required(login_url='login')
def dokumenpilih(request, prid):
    
    projetgetsebutid = project.Projek.objects.filter(id=prid).first()
    data = {
        'projek':project.Projek.objects.get(id=prid),
        'mrksatu':document.MRKSatu.objects.filter(projekbind=projetgetsebutid).first(),
        'mrkdua':document.MRKDua.objects.filter(projekbind=projetgetsebutid).first(),
        'lsk':document.Laporansiapkerja.objects.filter(projekbind=projetgetsebutid).first(),
        'mrktiga':document.MRKTiga.objects.filter(projekbind=projetgetsebutid).first(),
        'psk':document.PSK.objects.filter(projekbind=projetgetsebutid).first(),
        'ss':document.SenaraiSemakan.objects.filter(projekbind=projetgetsebutid).first(),
        'psmk':document.PSMK.objects.filter(projekbind=projetgetsebutid).first(),
        'pjb':document.SuratPJaminanbank.objects.filter(projekbind=projetgetsebutid).first(),
        'ppwjp':document.Perakuanpwjp.objects.filter(projekbind=projetgetsebutid).first(),
        'smrk':document.SuratMRK.objects.filter(projekbind=projetgetsebutid).first(),
        'skhas':document.SuratKhas.objects.filter(projekbind=projetgetsebutid).first(),
        'sbon':document.SuratPelepasanBon.objects.filter(projekbind=projetgetsebutid).first(),
        'scriptdoc':True
    }
    return render(request,  'pages/dokumennav.html',data)



@login_required(login_url='login')
def projekkodvot(request, kvd):

    userL = request.user.id
    print(userL)

    data = {
        'scriptvot':True,
        'senaraiprojek':project.Projek.objects.filter(kodvot=kvd),
        'kodvod':project.Projek.objects.filter(kodvot=kvd).first(),
        'ckodvot':project.Projek.objects.aggregate(
            total = Count('pk', filter=Q(kodvot=kvd)),
            sebutharga = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan='Sebutharga', kodvot=kvd)),
            undi = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan='Undi', kodvot=kvd)),
            lantikan = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan='Lantikan Terus', kodvot=kvd)),
        ),
    }

    return render(request, 'pages/maklumatkodvot.html',data)



#depend system
def load_sistem(request):

    sistemid = request.GET.get('sis_id')
    subsitem = project.subsistem.objects.filter(sistemlink=sistemid)
    return render(request, 'pages/loadsistem.html', {'subsitem': subsitem})

def load_component(request):

    subid = request.GET.get('sub_id')
    componentitem = project.komponen.objects.filter(subidlink=subid)
    return render(request, 'pages/loadcomponent.html', {'componentitem': componentitem})

