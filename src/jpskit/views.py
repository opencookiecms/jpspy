from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError

def index(request):
    return render(request, 'pages/maindashboard.html')

def kontraktordash(request):
    return render(request, 'pages/kontraktor-dashboard.html')

def kontraktorlist(request):
    return render(request, 'pages/kontraktor-list.html')

def kontraktordaftar(request):
    return render(request, 'pages/kontraktor-wizard.html' )

