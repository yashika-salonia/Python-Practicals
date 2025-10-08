from django.shortcuts import render
from . import templates

def indexPage(request):
    return render(request, 'index.html')

def aboutPage(request):
    return render(request, 'about.html')

def homePage(request):
    return render(request, 'home.html')