from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import kontraktor
from ..formcontroller import kontraktorform
from django.db.models import Q
from django.db.models import Count
from django.db.models.functions import NullIf
from django.core.exceptions import ObjectDoesNotExist



def kontraktordash(request):

    timecurrent = datetime.date.today().strftime('%d/%m/%Y')
  
    d = kontraktor.Kontraktor.objects.aggregate(
            kualamuda = Count('pk',filter=Q(konKawOperasi='Kuala Muda')),
            sik = Count('pk',filter=Q(konKawOperasi='Sik')),
            baling = Count('pk',filter=Q(konKawOperasi='Baling')),
            kedah = Count('pk',filter=Q(konKawOperasi='Kedah')),
        )
    t = kontraktor.Kontraktor.objects.aggregate(
            active = Count('pk', filter=Q(sijilJPSTamat__gte=timecurrent )),
            deactive = Count('pk', filter=Q(sijilJPSTamat__lte=timecurrent)),
        )
    
    g = kontraktor.Kontraktor.objects.aggregate(
            kualamuda = Count('pk', filter=Q(sijilPPKGredSatu='G1',konKawOperasi='Kuala Muda')),
            sik = Count('pk', filter=Q(sijilPPKGredSatu='G1',konKawOperasi='Sik')),
            baling = Count('pk', filter=Q(sijilPPKGredSatu='G1',konKawOperasi='Baling')),
  
            sikdactive = Count('pk', filter=Q(sijilPPKGredSatu='G1',sijilJPSTamat__gte=timecurrent,konKawOperasi='Sik')),
            balingdactive = Count('pk', filter=Q(sijilPPKGredSatu='G1',sijilJPSTamat__gte=timecurrent,konKawOperasi='Baling')),
            kualamudaactive = Count('pk', filter=Q(sijilPPKGredSatu='G1',sijilJPSTamat__gte=timecurrent,konKawOperasi='Kuala Muda')),

            sikdntactive = Count('pk', filter=Q(sijilPPKGredSatu='G1',sijilJPSTamat__lte=timecurrent,konKawOperasi='Sik')),
            balingdntactive = Count('pk', filter=Q(sijilPPKGredSatu='G1',sijilJPSTamat__lte=timecurrent,konKawOperasi='Baling')),
            kualamudantactive = Count('pk', filter=Q(sijilPPKGredSatu='G1',sijilJPSTamat__lte=timecurrent,konKawOperasi='Kuala Muda')),
        )
    
    data = {
        'titleboard':'Kontraktor Dashboard',
        'kontraktor':kontraktor.Kontraktor.objects.all(),
        'total':kontraktor.Kontraktor.objects.all().count(),
        'dateend' : timecurrent,
        'distict' : d,
        'totalactive':t,
        'g1total':g
    }

    return render(request, 'pages/kontraktor-dashboard.html',data)

def kontraktorprofile(request, kontrakid):

    data = {
        'kontraktor':kontraktor.Kontraktor.objects.get(pk=kontrakid),
    }
    return render(request, 'pages/kontraktor-profile.html',data)

def kontraktorlist(request):

    timecurrent = datetime.date.today().strftime('%d/%m/%Y')
    
    data = {
        'kontraktor':kontraktor.Kontraktor.objects.all(),
        'total':kontraktor.Kontraktor.objects.all().count(),
        'dateend' : timecurrent,
        'totalactive':kontraktor.Kontraktor.objects.aggregate(
            active = Count('pk', filter=Q(sijilJPSTamat__gte=timecurrent )),
            deactive = Count('pk', filter=Q(sijilJPSTamat__lte=timecurrent)),
        ),
    }

    return render(request, 'pages/kontraktor-list.html',data)

def kontraktordaftar(request):
    
    form = kontraktorform.KontraktroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = kontraktorform.KontraktroForm()
        
    else:
        print("no data was post yet")

    
    context = {
        'form':form
    }
    return render(request, 'pages/kontraktor-wizard.html',context )



def kontraktoredit(request, id):
    dataobj = kontraktor.Kontraktor.objects.get(id=id)
    form = kontraktorform.KontraktroForm(request.POST or None, request.FILES or None, instance=dataobj)
    if form.is_valid():
        form.save()
    else:
        pass

    data = {
        'form':form
    }

    return render(request, 'pages/kontraktor-edit.html',data)

def kontraktordelete(request, id):
    dataobj = kontraktor.Kontraktor.objects.get(id=id)
    dataobj.delete()

    if dataobj:
        return redirect('kontraktor/senarai')
    else:
        return render(request, 'pages/kontraktor-list.html')