from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse(f'[{request.path}] Home page')
