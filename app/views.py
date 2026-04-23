from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .services import get_all_movies, get_all_series, search_content
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def user_settings(request):
    return render(request, 'pages/user_settings.html')

def catalog(request):
    movies = get_all_movies()
    series = get_all_series()
    return render(request, 'pages/catalog.html', {'movies': movies, 'series': series})

def series(request):
    series=get_all_series()
    return render(request, 'pages/series.html', {'series': series} )

def movies(request):
    movies = get_all_movies()
    return render(request, '' \
    'pages/movies.html', {'movies': movies})

def search(request):
    query = request.GET.get('q', '').strip()
    movie_results = []
    series_results = []

def register(request):
    return render(request, 'streamsync_register.html',{
        'form': UserCreationForm
    })

def login(request):
    return render(request, 'login.html')
    if query:
        results = search_content(query)
        movie_results = [item for item in results if item.get('content_type') == 'movie']
        series_results = [item for item in results if item.get('content_type') == 'series']
        return render(request, 'pages/search.html', {
            'query' : query,
            'movies': movie_results,
            'series': series_results,
            'result_count': len(results)
        })
    
    return render(request, 'pages/search.html', {'query': ''})



def content_detail(request, ctype, cid):   
    
    if ctype == 'series':
        data = get_all_series()
    else:
        data = get_all_movies()
    content = next((item for item in data if str(item.get('id')) == str(cid)), None)
    # ... render
    if content:
        return render(request, 'pages/content_view.html', {'content': content})
    else:
        return render(request, 'pages/home.html', status=404)

def personal_library(request):
    return render(request, 'pages/personal_library.html')


def main(request):
    return render(request, 'pages/main.html')

@login_required
def login_redirect(request):
    user = request.user

    if user.is_superuser or user.groups.filter(name='administrator').exists():
        return redirect('app:movies') #provisional redirect

    elif user.groups.filter(name='technical').exists():
        return redirect('app:series') #provisional redirect
    
    elif user.groups.filter(name='plataform').exists():
        return redirect('app:series') #provisional redirect

    else:
        return redirect('app:main')
