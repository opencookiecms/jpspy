from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from .forms import KontraktroForm

def index(request):
    return render(request, 'pages/maindashboard.html')

def kontraktordash(request):
    return render(request, 'pages/kontraktor-dashboard.html')

def kontraktorlist(request):
    return render(request, 'pages/kontraktor-list.html')

def kontraktordaftar(request):

    form = KontraktroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = KontraktroForm()
        
    else:
        print(form)

    
    context = {
        'form':form
    }
    return render(request, 'pages/kontraktor-wizard.html',context )

