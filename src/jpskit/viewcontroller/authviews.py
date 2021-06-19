from django.shortcuts import render, get_list_or_404, redirect, reverse
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ..decorators import unautorized_user

@unautorized_user
def loginJPS(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =  request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'pages/login.html')

def logoutJPS(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
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