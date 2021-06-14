from django.shortcuts import render, get_list_or_404, redirect, reverse
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError,HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def login(request):
    return render(request, 'pages/login.html')