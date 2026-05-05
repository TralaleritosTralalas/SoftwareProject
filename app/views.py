from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .services import get_all_movies, get_all_series, search_content, get_movies_by_genres, get_series_by_genres, get_trending
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import VisualizationProgress
from django.utils.text import slugify

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def user_settings(request):
    return render(request, 'pages/user_settings.html')

def catalog(request):
    movies = get_all_movies()
    series = get_all_series()
    return render(request, 'pages/catalog.html', {'movies': movies, 'series': series})



def movies(request):
    movies = get_all_movies()
    for movie in movies:
        if 'unique_id' not in movie:
            from django.utils.text import slugify
            movie['unique_id'] = slugify(f"{movie.get('title', '')}_{movie.get('year', '')}")
    return render(request, 'pages/movies.html', {'movies': movies})

def series(request):
    series = get_all_series()
    for serie in series:
        if 'unique_id' not in serie:
            from django.utils.text import slugify
            serie['unique_id'] = slugify(f"{serie.get('title', '')}_{serie.get('start_year', '')}")
    return render(request, 'pages/series.html', {'series': series})

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

def search(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        results = search_content(query)
        movies_results = [item for item in results if item.get('content_type') == 'movie']
        series_results = [item for item in results if item.get('content_type') == 'series']
        
        return render(request, 'pages/search.html', {
            'query': query,
            'movies': movies_results,
            'series': series_results,
            'result_count': len(results)
        })
    
    return render(request, 'pages/search.html', {'query': ''})

def content_detail(request, ctype, cid):
    
    if ctype == 'series':
        data = get_all_series()
    else:
        data = get_all_movies()
    
    content = next((item for item in data if slugify(f"{item.get('title', '').replace(' ', '-')}_{item.get('year', item.get('start_year', ''))}") == slugify(str(cid))), None)
    
    if content:
        return render(request, 'pages/content_view.html', {'content': content})
    else:
        return render(request, 'pages/home.html', status=404)
    
def personal_library(request):
    return render(request, 'pages/personal_library.html')


@login_required
def main(request):
    user = request.user
    
    favorite_genres = list(user.favorite_genres.values_list('name', flat=True))
    
    recommended_by_genre = {}
    recommended_series_by_genre = {}
    if favorite_genres:
        recommended_by_genre = get_movies_by_genres(favorite_genres, min_total=5)
        recommended_series_by_genre = get_series_by_genres(favorite_genres, min_total=5)
    
    trending = get_trending(limit=4)
    
    watch_progress = VisualizationProgress.objects.filter(user=user, completed=False).select_related('content')
    has_watch_history = watch_progress.exists()
    
    return render(request, 'pages/main.html', {
        'recommended_by_genre': recommended_by_genre,
        'recommended_series_by_genre': recommended_series_by_genre,
        'trending': trending,
        'has_watch_history': has_watch_history,
        'watch_progress': watch_progress
    })

@login_required
def login_redirect(request):
    user = request.user

    if not user.onboarding_completed:
        return redirect('app:onboarding')

    if user.is_superuser or user.groups.filter(name='administrator').exists():
        return redirect('app:movies') #provisional redirect

    elif user.groups.filter(name='technical').exists():
        return redirect('app:series') #provisional redirect
    
    elif user.groups.filter(name='plataform').exists():
        return redirect('app:series') #provisional redirect

    else:
        return redirect('app:main')


@login_required
def onboarding(request):
    from app.models import Country
    
    if request.user.onboarding_completed:
        return redirect('app:main')
    
    if request.method == 'POST':
        birth_date = request.POST.get('birth_date')
        country_id = request.POST.get('country')
        gender = request.POST.get('gender')
        errors = []
        
        if not birth_date:
            errors.append('Date of birth is required')
        if not country_id:
            errors.append('Country is required')
        
        if errors:
            countries = Country.objects.all()
            return render(request, 'registration/onboarding.html', {
                'countries': countries,
                'errors': errors
            })
        
        user = request.user
        user.birth_date = birth_date
        user.country_id = country_id
        user.gender = gender if gender else None
        user.onboarding_completed = True
        user.save()
        
        return redirect('app:onboarding_genres')
    
    countries = Country.objects.all()
    return render(request, 'registration/onboarding.html', {
        'countries': countries
    })


@login_required
def onboarding_genres(request):
    from app.models import Genre
    
    if not request.user.onboarding_completed:
        return redirect('app:onboarding')
    
    if request.method == 'POST':
        selected_genres = request.POST.getlist('genres')
        
        if len(selected_genres) < 3:
            genres = Genre.objects.all()
            return render(request, 'registration/onboarding_genres.html', {
                'genres': genres,
                'error': f'Select at least 3 genres (you selected {len(selected_genres)})'
            })
        
        user = request.user
        user.favorite_genres.clear()
        for genre_id in selected_genres:
            try:
                genre = Genre.objects.get(id=genre_id)
                user.favorite_genres.add(genre)
            except Genre.DoesNotExist:
                pass
        
        return redirect('app:onboarding_complete')
    
    genres = Genre.objects.all()
    return render(request, 'registration/onboarding_genres.html', {
        'genres': genres
    })


@login_required
def onboarding_complete(request):
    if not request.user.onboarding_completed:
        return redirect('app:onboarding')
    return render(request, 'registration/onboarding_complete.html')
