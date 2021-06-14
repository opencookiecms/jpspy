from django.http import HttpResponse
from django.shortcuts import redirect

def unautorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        pass
    return wrapper_func