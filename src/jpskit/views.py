from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from .models import Kontraktor
from .forms import KontraktroForm, OrderForm

def index(request):
    return render(request, 'pages/maindashboard.html')

def kontraktordash(request):

    timecurrent = datetime.date.today().strftime('%d/%m/%Y')

    data = {
        'kontraktor':Kontraktor.objects.all(),
        'total':Kontraktor.objects.all().count(),
        'dateend' : timecurrent
    }

    return render(request, 'pages/kontraktor-dashboard.html',data)

def kontraktorlist(request):

    timecurrent = datetime.date.today().strftime('%d/%m/%Y')

    data = {
        'kontraktor':Kontraktor.objects.all(),
        'total':Kontraktor.objects.all().count(),
        'dateend' : timecurrent
    }

    return render(request, 'pages/kontraktor-list.html',data)

def kontraktordaftar(request):

    form = KontraktroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = KontraktroForm()
        
    else:
        print("no data was post yet")

    
    context = {
        'form':form
    }
    return render(request, 'pages/kontraktor-wizard.html',context )


def kontraktoredit(request, id):
    dataobj = Kontraktor.objects.get(id=id)
    form = KontraktroForm(request.POST or None, request.FILES or None, instance=dataobj)
    if form.is_valid():
        form.save()
    else:
        print(form)
     
    
    data = {
        'form':form
    }

    return render(request, 'pages/kontraktor-edit.html',data)

def kontraktordelete(request, id):
    dataobj = Kontraktor.objects.get(id=id)
    dataobj.delete()

    if dataobj:
        return redirect('kontraktor/senarai')
    else:
        return render(request, 'pages/kontraktor-list.html')

def ordersebutharga(request):

    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()
    else:
        print("the data was no save")
    
    data = {
        'form':form
    }
    return render(request, 'pages/order-add.html',data)


    

  

