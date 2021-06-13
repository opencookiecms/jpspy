from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import dfnoperolehan
from ..formcontroller import noperolehanform
from django.db.models import Q
from django.db.models import Count


def dnoperolehan(request):

    context = {
        'semua':dfnoperolehan.NoPerolehan.objects.filter(tarikh__year=2021),
        'sebutharga':dfnoperolehan.NoPerolehan.objects.filter(kaedahperolehan="Sebutharga", tarikh__year=2021),
        'lt':dfnoperolehan.NoPerolehan.objects.filter(kaedahperolehan="Lantikan Terus", tarikh__year=2021),
        'undi':dfnoperolehan.NoPerolehan.objects.filter(kaedahperolehan="Undi", tarikh__year=2021),
        'total':dfnoperolehan.NoPerolehan.objects.filter(tarikh__year=2021).count(),
        'kelas':dfnoperolehan.NoPerolehan.objects.aggregate(
            sebutharga = Count('pk', filter=Q(kaedahperolehan='Sebutharga', tarikh__year=2021)),
            lt = Count('pk', filter=Q(kaedahperolehan='Lantikan Terus', tarikh__year=2021)),
            undi = Count('pk', filter=Q(kaedahperolehan='Undi', tarikh__year=2021)),
        )
    }

    test = dfnoperolehan.NoPerolehan.objects.filter(tarikh__year=2021)
    print(test.query)
    return render(request, 'pages/noperolehan-dashboard.html',context)

    

def daftarnoperolehan(request):
    
    form = noperolehanform.DPerolehanForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = noperolehanform.DPerolehanForm()
        
    else:
        print("no data was post yet")
        print(form.errors)

    
    context = {
        'form':form
    }

    return render(request, 'pages/perolehan-daftar.html',context)

