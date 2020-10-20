from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError

def index(request):
    return render(request, 'pages/maindashboard.html')
