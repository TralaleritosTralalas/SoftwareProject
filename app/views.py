from django.shortcuts import render
from .services import get_all_movies

# Create your views here.

def home(request):
    return render(request, 'home.html')

def catalog(request):
    movies = get_all_movies()
    return render(request, 'catalog.html', {'movies': movies})
