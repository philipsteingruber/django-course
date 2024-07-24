from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')
