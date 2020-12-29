from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import kontraktor,dnoperolehan,order,project,userprofile
from ..formcontroller import noperolehanform, kontraktorform
from django.db.models import Q
from django.db.models import Count


def dnoperolehan(request):
    return render(request, 'pages/noperolehan-dashboard.html')



def daftarnoperolehan(request):
    
    form = noperolehanform.DPerolehanForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = noperolehanform.DPerolehanForm()
        
    else:
        print("no data was post yet")

    
    context = {
        'form':form
    }

    return render(request, 'pages/perolehan-daftar.html',context)
