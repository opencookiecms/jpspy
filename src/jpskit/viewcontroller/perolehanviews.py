from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import dfnoperolehan
from ..formcontroller import noperolehanform
from django.db.models import Q
from django.db.models import Count


def dnoperolehan(request):

    context = {
        'semua':dfnoperolehan.NoPerolehan.objects.all(),
        'sebutharga':dfnoperolehan.NoPerolehan.objects.filter(kaedahperolehan="Sebutharga"),
        'lt':dfnoperolehan.NoPerolehan.objects.filter(kaedahperolehan="Lantikan Terus"),
        'undi':dfnoperolehan.NoPerolehan.objects.filter(kaedahperolehan="Undi"),
        'total':dfnoperolehan.NoPerolehan.objects.all().count(),
        'kelas':dfnoperolehan.NoPerolehan.objects.aggregate(
            sebutharga = Count('pk', filter=Q(kaedahperolehan='Sebutharga')),
            lt = Count('pk', filter=Q(kaedahperolehan='Lantikan Terus')),
            undi = Count('pk', filter=Q(kaedahperolehan='Undi')),
        )
    }
    return render(request, 'pages/noperolehan-dashboard.html',context)



def daftarnoperolehan(request):
    
    form = noperolehanform.DPerolehanForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = noperolehanform.DPerolehanForm()
        
    else:
        print("no data was post yet")
        print(form)

    
    context = {
        'form':form
    }

    return render(request, 'pages/perolehan-daftar.html',context)

