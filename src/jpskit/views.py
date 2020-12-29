from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from django.db.models import Q
from django.db.models import Count


def index(request):
    return render(request, 'pages/maindashboard.html')











    

  

