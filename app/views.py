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
    
def get_content_by_id(content_id):
    movies = get_all_movies()
    series = get_all_series()
    all_content = movies + series

    for content in all_content:
        if str(content.get('id')) == str(content_id):
            return content
    return None

def content_detail(request, content_id):   
    content = get_content_by_id(content_id)
    if content:
        return render(request, 'pages/content_view.html', {'content': content})
    else:
        return render(request, 'pages/home.html', status=404)



def main(request):
    return render(request, 'pages/main.html')