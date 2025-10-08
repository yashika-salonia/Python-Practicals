from django.shortcuts import render
from . import templates

def homePage(request):
    return render(request, 'home.html')

def indexPage(request):
    return render(request, 'index.html')