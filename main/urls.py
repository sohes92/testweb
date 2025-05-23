from django.urls import path
from django.shortcuts import render

def home(request):
    return render(request, 'testweb/index.html')

urlpatterns = [
    path('', home, name='home'),
]