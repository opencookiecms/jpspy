from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError,HttpResponseRedirect
from ..modelcontroller import document,dfnoperolehan,kontraktor,project
from ..formcontroller import ducumentform
from django.db.models import Q
from django.db.models import Count
from django.contrib.auth.models import User


def mrkone(request, idperolehan):
 
    dataobject = document.MRKSatu.objects.filter(mrksatunosebutharga=idperolehan).first()
    datasbut = dfnoperolehan.NoPerolehan.objects.get(id=idperolehan)
    print(datasbut)
    form = ducumentform.MRK1Form(request.POST or None, instance=dataobject)

    kos_belanjapost = 0.00
    kos_tanggungpost =  request.POST.get('mrksatukosprojek')
  
    if form.is_valid():

        if(dataobject):
            query = document.kosprojek.objects.get(kos_sebutharga=datasbut)
            query.kos_tanggung = kos_tanggungpost
            query.kos_belanja = kos_belanjapost
            query.save()
          
        else:
            query = document.kosprojek.objects.create(kos_belanja=kos_belanjapost,kos_tanggung=kos_tanggungpost,kos_sebutharga=datasbut)
            query.save()

        form.save()
        form = ducumentform.MRK1Form()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  
    else:
        print(form.errors)
      

    context = {
        'form':form,
        'sebutharga':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'kontraktor':kontraktor.Kontraktor.objects.all(),
        'kursus':document.MRKKursus.objects.all(),
        'mrksatu':document.MRKSatu.objects.filter(mrksatunosebutharga=idperolehan).first()
    }
    return render(request, 'pages/mrksatu.html',context )



def mrktwo(request, idperolehan):
    
    dataobject = document.MRKDua.objects.filter(mrkduanosebutharga=idperolehan).first()
    form = ducumentform.MRKDuaForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        form.save()
        form = ducumentform.MRKDuaForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    
    else:
        print("no data was save")
        print(form)
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.filter(mrksatunosebutharga=idperolehan).first(),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
    }

    
    return render(request, 'pages/mrkdua.html',context)

def laporansiapkerja(request, idperolehan ):

    dataobject = document.Laporansiapkerja.objects.filter(lsknosebutharga=idperolehan).first()

    form = ducumentform.LSKForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        form.save()
        form = ducumentform.LSKForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   
    else:
        print(form.errors)

    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/lsk.html',context)

def mrktiga(request, idperolehan):

    dataobject = document.MRKTiga.objects.filter(mrktigasebutharga=idperolehan).first()
    form = ducumentform.MRKtigaForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        form.save()
        form = ducumentform.MRKtigaForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("no data was save")
        print(form)

    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/mrktiga.html',context)

def psk(request, idperolehan):
    dataobject = document.PSK.objects.filter(psknosebutharga=idperolehan).first()
    form = ducumentform.PSKForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        form.save()
        form = ducumentform.PSKForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save yet")
        print(form)

    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }
    

    return render(request, 'pages/psk.html',context)


def ssv(request, idperolehan):
    dataobject = document.SenaraiSemakan.objects.filter(ssnosebutharga=idperolehan).first()
    form = ducumentform.SenaraiSemakanForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        form.save()
        form = ducumentform.SenaraiSemakanForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save yet")
        print(form)

    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }
    

    return render(request, 'pages/senaraisemakan.html',context)

def psmkview(request, idperolehan):
    dataobject = document.PSMK.objects.filter(psmknosebutharga=idperolehan).first()
    form = ducumentform.Psmkform(request.POST or None, instance=dataobject)
 
    if form.is_valid():
        form.save()
        form = ducumentform.Psmkform()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save yet")
        print(form)
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/psmk.html',context)

def jaminanbankv(request, idperolehan):
    dataobject = document.SuratPJaminanbank.objects.filter(jbankknosebutharga=idperolehan).first()
    form = ducumentform.JaminanBankForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.JaminanBankForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save")
        print(form)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/jaminanbank.html',context)

def pwjpview(request, idperolehan):
    dataobject = document.Perakuanpwjp.objects.filter(wjpknosebutharga=idperolehan).first()
    form = ducumentform.PwjpForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.PwjpForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save")
        print(form)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/ppwjp.html',context)


def smrkview(request, idperolehan):
    dataobject = document.SuratMRK.objects.filter(smrkknosebutharga=idperolehan).first()
    form = ducumentform.SuratMRKForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.SuratMRKForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save")
        print(form)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/smrk.html',context)

def skhasview(request, idperolehan):
    dataobject = document.SuratKhas.objects.filter(khasknosebutharga=idperolehan).first()
    form = ducumentform.SuratKhasForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.SuratKhasForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save")
        print(form)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/skhas.html',context)


def sbonview(request, idperolehan):
    dataobject = document.SuratPelepasanBon.objects.filter(bonknosebutharga=idperolehan).first()
    form = ducumentform.SuratBonForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.SuratBonForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save")
        print(form)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(mrksatunosebutharga=idperolehan),
        'projek':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/sbon.html',context)
     
 
        


    
