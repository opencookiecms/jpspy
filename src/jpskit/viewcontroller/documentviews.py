from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import document,dfnoperolehan,kontraktor,project
from ..formcontroller import ducumentform
from django.db.models import Q
from django.db.models import Count
from django.contrib.auth.models import User


def mrkoneregister(request, idperolehan):
    
    form = ducumentform.MRK1Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = ducumentform.MRK1Form()
        return redirect('projek/senarai') 
        
    else:
        print("no data was post yet")
        print(form)

    
    context = {
        'form':form,
        'sebutharga':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'kontraktor':kontraktor.Kontraktor.objects.all(),
        'kursus':document.MRKKursus.objects.all()
    }
    return render(request, 'pages/mrksatu.html',context )

def mrktworegister(request, idperolehan):

    form = ducumentform.MRKDuaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ducumentform.MRKDuaForm()
        return redirect('projek/senarai')
    
    else:
        print("no data was save")
        print(form)
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
    }

    
    return render(request, 'pages/mrkdua.html',context)

def laporansiapkerja(request, idperolehan ):

    form = ducumentform.LSKForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ducumentform.LSKForm()
        return redirect('projek/senarai')
    else:
        print("no data was save")
        print(form)

    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/lsk.html',context)

    
