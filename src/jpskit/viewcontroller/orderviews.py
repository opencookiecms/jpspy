from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import order
from ..formcontroller import  orderform
from django.db.models import Q
from django.db.models import Count




def ordersebutharga(request):
    
    form = orderform.OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = orderform.OrderForm()
    else:
        print("the data was no save")
    
    data = {
        'form':form
    }
    return render(request, 'pages/order-add.html',data)

