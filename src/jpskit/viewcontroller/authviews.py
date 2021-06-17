from django.shortcuts import render, get_list_or_404, redirect, reverse
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError,HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


def loginJPS(request):
    return render(request, 'pages/login.html')

def registerJPS(request):
    form  = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {
        'form':form
    }
    return render(request, 'pages/register.html',context)