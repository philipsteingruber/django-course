from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def register_user(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/register.html')
