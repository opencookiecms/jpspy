from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import project,dfnoperolehan,document
from ..formcontroller import projekform
from django.db.models import Q
from django.db.models import Count


def daftarprojek(request):
    
    form = projekform.Projekform(request.POST or None)
    if form.is_valid():
        form.save()
        form = projekform.Projekform()
        return redirect('projek/senarai')  
        
    else:
        print("no data was post yet")
        print(form)

    
    context = {
        'form':form,
        'sungai':project.isSungai.objects.all(),
        'sebutharga': dfnoperolehan.NoPerolehan.objects.all(),
    }

    return render(request, 'pages/projek-daftar.html',context)

def maklumatperolehan(request):

    data = {
        'senaraiprojek':project.Projek.objects.all(),
        'totalprojek':project.Projek.objects.all().count(),
        'kodvod':project.Projek.objects.values('kodvot').annotate(jumlah=Count('kodvot')),
        'total':project.Projek.objects.aggregate(
            sebutharga = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan='Sebutharga')),
            undi = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan='Undi')),
            lantikan = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan='Lantikan Terus')),
        ), 
    }
    return render(request, 'pages/maklumatperolehandash.html',data)

def maklumatperolehanjenis(request, jenisp):

    data = {
        'senaraiprojek':project.Projek.objects.filter(nosebuthargaid__kaedahperolehan=jenisp).annotate(total=Count('kodvot')),
        'kodvod':project.Projek.objects.filter(nosebuthargaid__kaedahperolehan=jenisp).annotate(jumlah=Count('kodvot')),
        'totalprojek':project.Projek.objects.all().count(),
        'total':project.Projek.objects.aggregate(
            sebutharga = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan="Sebutharga")),
            undi = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan="Undi")),
            lantikan = Count('pk', filter=Q(nosebuthargaid__kaedahperolehan="Lantikan Terus")),
        ),
    }

    return render(request, 'pages/maklumatperolehandash.html',data)

def senaraiprojek(request):

    data = {
        'senaraiprojek':project.Projek.objects.all()
    }

    return render(request, 'pages/projek-senarai.html',data)


def dokumenpilih(request, prid):
    
    projetgetsebutid = project.Projek.objects.filter(id=prid).first()
    data = {
        'projek':project.Projek.objects.get(id=prid),
        'mrksatu':document.MRKSatu.objects.filter(mrksatunosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'mrkdua':document.MRKDua.objects.filter(mrkduanosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'lsk':document.Laporansiapkerja.objects.filter(lsknosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'mrktiga':document.MRKTiga.objects.filter(mrktigasebutharga=projetgetsebutid.nosebuthargaid).first(),
        'psk':document.PSK.objects.filter(psknosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'ss':document.SenaraiSemakan.objects.filter(ssnosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'psmk':document.PSMK.objects.filter(psmknosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'pjb':document.SuratPJaminanbank.objects.filter(jbankknosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'ppwjp':document.Perakuanpwjp.objects.filter(wjpknosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'smrk':document.SuratMRK.objects.filter(smrkknosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'skhas':document.SuratKhas.objects.filter(khasknosebutharga=projetgetsebutid.nosebuthargaid).first(),
        'sbon':document.SuratPelepasanBon.objects.filter(bonknosebutharga=projetgetsebutid.nosebuthargaid).first(),
    }
    return render(request,  'pages/dokumennav.html',data)

def projekkodvot(request, kvd):

    data = {
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

    #sistemid = request.GET.get('sistemid')
    subsitem = project.subsistem.objects.filter(sistemlink=2)
    return render(request, 'pages/dropdowntest.html', {'subsitem': subsitem})

