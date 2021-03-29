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
        'sebutharga': dfnoperolehan.NoPerolehan.objects.all(),
    }

    return render(request, 'pages/projek-daftar.html',context)

def maklumatperolehan(request):

    data = {
        'senaraiprojek':project.Projek.objects.all(),
        'kodvod':project.Projek.objects.values('kodvot').annotate(jumlah=Count('kodvot'))
        
    }
    return render(request, 'pages/maklumatperolehandash.html',data)

def maklumatperolehanjenis(request, strjenis):

    data = {
        'senaraiprojek':project.Projek.objects.filter(nosebuthargaid__kaedahperolehan=strjenis).annotate(total=Count('kodvot')),
        'kodvod':project.Projek.objects.filter(nosebuthargaid__kaedahperolehan=strjenis).annotate(jumlah=Count('kodvot')) 
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
    }
    return render(request,  'pages/dokumennav.html',data)

