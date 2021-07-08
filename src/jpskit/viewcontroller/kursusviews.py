from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from ..modelcontroller import kursus
from ..formcontroller import  orderform
from django.db.models import Q
from django.db.models import Count




def kursusdashboard(request):
    return render(request, 'pages/kursusdashboard.html')


def kursusdaftar(request):
    return render(request,'pages/kursusdaftar.html')

