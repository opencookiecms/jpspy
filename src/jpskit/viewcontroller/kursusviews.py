from django import forms
from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError,HttpResponseRedirect
from ..modelcontroller import kursus
from ..formcontroller import  kursusforms
from django.db.models import Q
from django.db.models import Count




def kursusdashboard(request):

    data = {
        'total':kursus.Course.objects.all().count(),
        'kursus':kursus.Course.objects.all(), 
    }
    return render(request, 'pages/kursusdashboard.html',data)


def kursusdaftar(request):

    form = kursusforms.Dkursusform(request.POST or None)

    if form.is_valid():
        form.save()
        form = kursusforms.Dkursusform()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print(form.errors)
    
    data = {
        'form':form
    }

    return render(request,'pages/kursusdaftar.html',data)

