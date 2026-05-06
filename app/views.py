from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .services import get_all_movies, get_all_series, search_content, get_movies_by_genres, get_series_by_genres, get_trending, get_all_platforms, get_all_genres_from_api, search_content
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
    # Obtener parámetros de filtro
    selected_platform = request.GET.get('platform')
    selected_genre = request.GET.get('genre')
    sort_rating = request.GET.get('sort_rating')
    sort_year = request.GET.get('sort_year')

    # Obtener datos base
    movies = get_all_movies(platform_filter=selected_platform)
    series = get_all_series(platform_filter=selected_platform)
    
    # Filtrar por género localmente si se seleccionó uno
    if selected_genre:
        movies = [m for m in movies if m.get('genre_name') == selected_genre]
        series = [s for s in series if s.get('genre_name') == selected_genre]

    # Lógica de ordenamiento
    def apply_sort(data, key_rating, key_year):
        if sort_rating:
            data.sort(key=lambda x: x.get(key_rating, 0), reverse=(sort_rating == 'desc'))
        if sort_year:
            data.sort(key=lambda x: x.get(key_year, 0), reverse=(sort_year == 'desc'))
        return data

    movies = apply_sort(movies, 'rating', 'year')
    series = apply_sort(series, 'rating', 'start_year')

    context = {
        'movies': movies,
        'series': series,
        'platforms': get_all_platforms(),
        'genres': get_all_genres_from_api(),
        'selected_platform': selected_platform,
        'selected_genre': selected_genre,
        'sort_rating': sort_rating,
        'sort_year': sort_year,
    }
    return render(request, 'pages/catalog.html', context)

def movies(request):
    selected_platform = request.GET.get('platform')
    selected_genre = request.GET.get('genre')
    sort_rating = request.GET.get('sort_rating')
    sort_year = request.GET.get('sort_year')

    movies_list = get_all_movies(platform_filter=selected_platform)
    
    # Filtrado por género
    if selected_genre:
        movies_list = [m for m in movies_list if m.get('genre_name') == selected_genre]

    # Ordenamiento
    if sort_rating:
        movies_list.sort(key=lambda x: x.get('rating', 0), reverse=(sort_rating == 'desc'))
    if sort_year:
        movies_list.sort(key=lambda x: x.get('year', 0), reverse=(sort_year == 'desc'))

    context = {
        'movies': movies_list,
        'platforms': get_all_platforms(), # <--- Añadir esto
        'genres': get_all_genres_from_api(), # <--- Añadir esto
        'selected_platform': selected_platform,
        'selected_genre': selected_genre,
        'sort_rating': sort_rating,
        'sort_year': sort_year,
    }
    return render(request, 'pages/movies.html', context)

def series(request):
    selected_platform = request.GET.get('platform')
    selected_genre = request.GET.get('genre')
    sort_rating = request.GET.get('sort_rating')
    sort_year = request.GET.get('sort_year')

    series_list = get_all_series(platform_filter=selected_platform)
    
    # Filtrado por género
    if selected_genre:
        series_list = [s for s in series_list if s.get('genre_name') == selected_genre]

    # Ordenamiento
    if sort_rating:
        series_list.sort(key=lambda x: x.get('rating', 0), reverse=(sort_rating == 'desc'))
    if sort_year:
        series_list.sort(key=lambda x: x.get('start_year', 0), reverse=(sort_year == 'desc'))

    context = {
        'series': series_list,
        'platforms': get_all_platforms(), # <--- Añadir esto
        'genres': get_all_genres_from_api(), # <--- Añadir esto
        'selected_platform': selected_platform,
        'selected_genre': selected_genre,
        'sort_rating': sort_rating,
        'sort_year': sort_year,
    }
    return render(request, 'pages/series.html', context)

def search(request):
    query = request.GET.get('q', '').strip()
    p = request.GET.get('platform')
    g = request.GET.get('genre')
    sr = request.GET.get('sort_rating')
    sy = request.GET.get('sort_year')
    
    results = []
    if query:
        # Ahora el servicio devuelve objetos con el campo 'detail_url' ya calculado
        results = search_content(query, platform=p, genre=g, sort_rating=sr, sort_year=sy)

    context = {
        'query': query,
        'movies': [i for i in results if i['content_type'] == 'movie'],
        'series': [i for i in results if i['content_type'] == 'series'],
        'result_count': len(results),
        'platforms': get_all_platforms(),
        'genres': get_all_genres_from_api(),
        'selected_platform': p,
        'selected_genre': g,
    }
    return render(request, 'pages/search.html', context)

def register(request):
    return render(request, 'streamsync_register.html',{
        'form': UserCreationForm
    })

def login(request):
    return render(request, 'login.html')


def content_detail(request, ctype, cid):
    from django.http import JsonResponse
    from .models import VisualizationProgress, Favorite, Watchlist
    
    if ctype == 'series':
        data = get_all_series()
    else:
        data = get_all_movies()
    
    content = next((item for item in data if slugify(f"{item.get('title', '').replace(' ', '-')}_{item.get('year', item.get('start_year', ''))}") == slugify(str(cid))), None)
    
    if content:
        content['content_type'] = ctype
        
        # Obtener estado del usuario si está autenticado
        user_status = 'not_seen'
        is_favorite = False
        is_in_watchlist = False
        
        if request.user.is_authenticated:
            # Buscar el contenido en la base de datos local
            from app.models import AudiovisualContent, Movie, Series
            try:
                if ctype == 'series':
                    local_content = Series.objects.filter(title=content.get('title')).first()
                else:
                    local_content = Movie.objects.filter(title=content.get('title')).first()
                
                if local_content:
                    # Verificar VisualizationProgress
                    vp = VisualizationProgress.objects.filter(user=request.user, content=local_content).first()
                    if vp:
                        if vp.completed:
                            user_status = 'completed'
                        elif vp.last_minute > 0:
                            user_status = 'watching'
                    
                    # Verificar Favorite
                    is_favorite = Favorite.objects.filter(user=request.user, content=local_content).exists()
                    
                    # Verificar Watchlist
                    is_in_watchlist = Watchlist.objects.filter(user=request.user, content=local_content).exists()
            except Exception:
                pass
        
        return render(request, 'pages/content_view.html', {
            'content': content,
            'user_status': user_status,
            'is_favorite': is_favorite,
            'is_in_watchlist': is_in_watchlist
        })
    else:
        return render(request, 'pages/home.html', status=404)


@login_required
def update_status(request, ctype, cid):
    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from django.utils.decorators import method_decorator
    from .models import VisualizationProgress, Movie, Series
    import json
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            status = data.get('status', 'not_seen')
            
            # Buscar contenido local
            if ctype == 'series':
                local_content = Series.objects.filter(title__icontains=cid.replace('-', ' ').split('_')[0]).first()
            else:
                local_content = Movie.objects.filter(title__icontains=cid.replace('-', ' ').split('_')[0]).first()
            
            if local_content:
                vp, created = VisualizationProgress.objects.get_or_create(
                    user=request.user,
                    content=local_content
                )
                
                if status == 'completed':
                    vp.completed = True
                    vp.last_minute = local_content.duration_minutes if hasattr(local_content, 'duration_minutes') else 0
                elif status == 'watching':
                    vp.completed = False
                    vp.last_minute = vp.last_minute if vp.last_minute > 0 else 1
                else:  # not_seen
                    vp.completed = False
                    vp.last_minute = 0
                
                vp.save()
                
                return JsonResponse({'success': True, 'status': status})
            
            return JsonResponse({'success': False, 'error': 'Content not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid method'})


@login_required
def toggle_favorite(request, ctype, cid):
    from django.http import JsonResponse
    from .models import Favorite, Movie, Series
    import json
    
    if request.method == 'POST':
        try:
            # Buscar contenido local
            if ctype == 'series':
                local_content = Series.objects.filter(title__icontains=cid.replace('-', ' ').split('_')[0]).first()
            else:
                local_content = Movie.objects.filter(title__icontains=cid.replace('-', ' ').split('_')[0]).first()
            
            if local_content:
                favorite = Favorite.objects.filter(user=request.user, content=local_content).first()
                if favorite:
                    favorite.delete()
                    return JsonResponse({'success': True, 'is_favorite': False})
                else:
                    Favorite.objects.create(user=request.user, content=local_content)
                    return JsonResponse({'success': True, 'is_favorite': True})
            
            return JsonResponse({'success': False, 'error': 'Content not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid method'})
    
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
