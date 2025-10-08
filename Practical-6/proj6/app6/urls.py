from django.urls import path 
from . import views
urlpatterns=[
    path('',views.homePage,name='home'),
    path('index/',views.indexPage,name='index')
]