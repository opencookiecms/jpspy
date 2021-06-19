from django.shortcuts import render, get_list_or_404, redirect, reverse
import datetime
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError
from django.db.models import Q
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unautorized_user
from django.contrib.auth import authenticate



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def index(request):

    context = {
        'test':'test value'
    }
    return render(request, 'pages/maindashboard.html',context)











    

  

