from django.shortcuts import render
from .services import get_all_movies, get_all_series, search_content

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

    if query:
        results = search_content(query)
        return render(request, 'pages/search.html', {
            'query' : query,
            'results' : results
        })
    
def content_detail(request, content_id):
    movies = get_all_movies()
    series = get_all_series()
    content = next((item for item in movies + series if item['id'] == content_id), None)

    if content:
        return render(request, 'pages/content_detail.html', {'content': content})
    else:
        return render(request, 'pages/content_not_found.html', status=404)



def main(request):
    return render(request, 'pages/main.html')