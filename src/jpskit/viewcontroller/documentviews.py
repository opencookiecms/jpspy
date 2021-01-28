from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import document,dfnoperolehan,kontraktor,project
from ..formcontroller import ducumentform
from django.db.models import Q
from django.db.models import Count


def mrkoneregister(request, idperolehan):
    
    form = ducumentform.MRK1Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ducumentform.MRK1Form()
        
    else:
        print("no data was post yet")

    
    context = {
        'form':form,
        'sebutharga':project.Projek.objects.get(nosebuthargaid=idperolehan),
        'kontraktor':kontraktor.Kontraktor.objects.all(),
        'kursus':document.MRKKursus.objects.all()
    }
    return render(request, 'pages/mrksatu-reg.html',context )
    
