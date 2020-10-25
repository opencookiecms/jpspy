from django.shortcuts import render
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from .models import Kontraktor
from .forms import KontraktroForm

def index(request):
    return render(request, 'pages/maindashboard.html')

def kontraktordash(request):
    return render(request, 'pages/kontraktor-dashboard.html')

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

