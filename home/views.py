from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'home.html')


def wip_page(request):
    return render(request, 'wip.html')
