from django.urls import path
from . import views

urlpatterns=[
    path('', views.indexPage, name='index'),
    path('about/', views.aboutPage, name='about'),
    path('home/', views.homePage, name='home'),
]