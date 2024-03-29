from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError,HttpResponseRedirect
from ..modelcontroller import document,dfnoperolehan,kontraktor,project
from ..formcontroller import ducumentform
from django.db.models import Q
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import uuid

@login_required(login_url='login')
def mrkone(request, projekid):


    dataobject = document.MRKSatu.objects.filter(projekbind=projekid).first()
    p = project.Projek.objects.get(id=projekid)
    print(p)
   
    form = ducumentform.MRK1Form(request.POST or None, instance=dataobject)

    kos_belanjapost = 0.00
    kos_tanggungpost =  request.POST.get('mrksatukosprojek')
  
    if form.is_valid():

        if(dataobject):
            query = document.kosprojek.objects.get(projekbind=p)
            query.kos_tanggung = kos_tanggungpost
            query.kos_belanja = kos_belanjapost
            query.save()
          
        else:
            query = document.kosprojek.objects.create(kos_belanja=kos_belanjapost,kos_tanggung=kos_tanggungpost,projekbind=p)
            query.save()

        form.save()
        form = ducumentform.MRK1Form()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  
    else:
        print(form.errors)
      

    context = {
    
        'form':form,
        'projek':project.Projek.objects.get(id=projekid),
        'kontraktor':kontraktor.Kontraktor.objects.all(),
        'mrksatu':dataobject,
        'stepstep':'3'

    }
    return render(request, 'pages/mrksatu.html',context )



@login_required(login_url='login')
def mrktwo(request, projekid):
    
    dataobject = document.MRKDua.objects.filter(projekbind=projekid).first()
    form = ducumentform.MRKDuaForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        form.save()
        form = ducumentform.MRKDuaForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    
    else:
        print("no data was save")
        print(form.errors)
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.filter(projekbind=projekid).first(), 
        'projek':project.Projek.objects.get(id=projekid),
        'stepstep':'5'
        
    }

    
    return render(request, 'pages/mrkdua.html',context)

@login_required(login_url='login')
def laporansiapkerja(request, projekid ):

    dataobject = document.Laporansiapkerja.objects.filter(projekbind=projekid).first()
    p = project.Projek.objects.get(id=projekid)

    kos_belanjasebenar = request.POST.get('lskhargasebenar')
    kos_tanggungpost =  0.00
   
    form = ducumentform.LSKForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        query = document.kosprojek.objects.get(projekbind=p)
        query.kos_tanggung = kos_tanggungpost
        query.kos_belanja = kos_belanjasebenar
        query.save()
        form.save()
        form = ducumentform.LSKForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   
    else:
        print(form.errors)

    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/lsk.html',context)


@login_required(login_url='login')
def mrktiga(request, projekid):

    dataobject = document.MRKTiga.objects.filter(projekbind=projekid).first()
    form = ducumentform.MRKtigaForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        form.save()
        form = ducumentform.MRKtigaForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("no data was save")
        print(form.errors)

    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'lskfecth':document.Laporansiapkerja.objects.get(projekbind=projekid),
        'mrkduafecth':document.MRKDua.objects.get(projekbind=projekid),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all(),
        'stepstep':'12',
    }

    return render(request, 'pages/mrktiga.html',context)

@login_required(login_url='login')
def psk(request, projekid):
    dataobject = document.PSK.objects.filter(projekbind=projekid).first()
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
        'lskfecth':document.Laporansiapkerja.objects.get(projekbind=projekid),
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all()
    }
    

    return render(request, 'pages/psk.html',context)

@login_required(login_url='login')
def ssv(request, projekid):
    
    dataobject = document.SenaraiSemakan.objects.filter(projekbind=projekid).first()
    form = ducumentform.SenaraiSemakanForm(request.POST or None, instance=dataobject)
    if form.is_valid():
        form.save()
        form = ducumentform.SenaraiSemakanForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save yet")
        print(form.errors)

    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all()
    }
    

    return render(request, 'pages/senaraisemakan.html',context)

@login_required(login_url='login')
def psmkview(request, projekid):
    dataobject = document.PSMK.objects.filter(projekbind=projekid).first()
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
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'pskfecth':document.PSK.objects.filter(projekbind=projekid).first(),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/psmk.html',context)

@login_required(login_url='login')
def jaminanbankv(request, projekid):
    dataobject = document.SuratPJaminanbank.objects.filter(projekbind=projekid).first()
    form = ducumentform.JaminanBankForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.JaminanBankForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print(form.errors)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all(),
        'pskfecth':document.PSK.objects.filter(projekbind=projekid).first(),
        'psmkfecth':document.PSMK.objects.filter(projekbind=projekid).first(),
    }

    return render(request, 'pages/jaminanbank.html',context)


@login_required(login_url='login')
def pwjpview(request, projekid):
    dataobject = document.Perakuanpwjp.objects.filter(projekbind=projekid).first()
    form = ducumentform.PwjpForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.PwjpForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save")
        print(form.errors)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/ppwjp.html',context)

@login_required(login_url='login')
def smrkview(request, projekid):
    dataobject = document.SuratMRK.objects.filter(projekbind=projekid).first()
    form = ducumentform.SuratMRKForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.SuratMRKForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save")
        print(form.errors)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/smrk.html',context)

@login_required(login_url='login')
def skhasview(request, projekid):
    dataobject = document.SuratKhas.objects.filter(projekbind=projekid).first()
    form = ducumentform.SuratKhasForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.SuratKhasForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save")
        print(form.errors)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/skhas.html',context)

@login_required(login_url='login')
def sbonview(request, projekid):
    dataobject = document.SuratPelepasanBon.objects.filter(projekbind=projekid).first()
    form = ducumentform.SuratBonForm(request.POST or None, instance=dataobject)

    if form.is_valid():
        form.save()
        form = ducumentform.SuratBonForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("data was not save")
        print(form.errors)
    
    
    context = {
        'form':form,
        'mrksatufecth':document.MRKSatu.objects.get(projekbind=projekid),
        'projek':project.Projek.objects.get(id=projekid),
        'userlist':User.objects.all()
    }

    return render(request, 'pages/sbon.html',context)
     
 
        


    
