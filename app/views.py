from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .services import get_all_movies, get_all_series, search_content
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def catalog(request):
    movies = get_all_movies()
    series = get_all_series()
    return render(request, 'pages/catalog.html', {'movies': movies, 'series': series})

def series(request):
    series=get_all_series()
    return render(request, 'pages/series.html', {'series': series} )

def movies(request):
    movies = get_all_movies()
    return render(request, 'pages/movies.html', {'movies': movies})

def search(request):
    query = request.GET.get('q', '').strip()
    results = []

def register(request):
    return render(request, 'streamsync_register.html',{
        'form': UserCreationForm
    })

def login(request):
    return render(request, 'login.html')
    if query:
        results = search_content(query)
        return render(request, 'pages/search.html', {
            'query' : query,
            'results' : results
        })


def main(request):
    return render(request, 'pages/main.html')


@login_required
@user_passes_test(lambda u: u.profile.role == 'Tech' or u.profile.role == 'Admin')
def tech(request):
    return render(request, 'pages/tech.html')