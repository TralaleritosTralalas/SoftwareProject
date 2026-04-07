from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'streamsync_register.html')

def login(request):
    return render(request, 'login.html')