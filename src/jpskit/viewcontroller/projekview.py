from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import project,dfnoperolehan
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

def senaraiprojek(request):

    data = {
        'senaraiprojek':project.Projek.objects.all()
    }

    return render(request, 'pages/projek-senarai.html',data)


def dokumenpilih(request, prid):

    data = {
        'projek':project.Projek.objects.get(id=prid),
    }
    return render(request,  'pages/dokumennav.html',data)

