from django.contrib.auth.forms import UserCreationForm
from .services import get_all_movies, get_all_series, search_content, get_movies_by_genres, get_series_by_genres, get_trending, get_all_platforms, get_all_genres_from_api, search_content
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, logout
from .models import VisualizationProgress
from django.utils.text import slugify
from app.models import Country
from app.models import User, Country
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Count
from django.core.exceptions import PermissionDenied
from .models import *
from .utils import DashboardService
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import VisualizationProgress, Movie, Series
import json
    
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

@login_required
def user_settings(request):


    countries = Country.objects.all()

    if request.method == 'POST':
        user = request.user

        if request.POST.get('action') == 'change_password':
            current_password = request.POST.get('current_password', '').strip()
            new_password = request.POST.get('new_password', '').strip()
            confirm_password = request.POST.get('confirm_password', '').strip()

            password_errors = []

            if not current_password:
                password_errors.append('Current password is required')
            elif not user.check_password(current_password):
                password_errors.append('Current password is incorrect')

            if not new_password:
                password_errors.append('New password is required')
            elif len(new_password) < 8:
                password_errors.append('New password must be at least 8 characters')

            if new_password != confirm_password:
                password_errors.append('New password and confirm password do not match')

            if password_errors:
                return render(request, 'pages/user_settings.html', {
                    'user': user,
                    'countries': countries,
                    'password_errors': password_errors
                })

            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)

            return render(request, 'pages/user_settings.html', {
                'user': user,
                'countries': countries,
                'password_success': 'Password changed successfully!'
            })

        username = request.POST.get('username', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        bio = request.POST.get('bio', '').strip()
        gender = request.POST.get('gender')
        country_id = request.POST.get('country')

        errors = []

        if not username:
            errors.append('Username is required')
        elif username != user.username and User.objects.filter(username=username).exclude(pk=user.pk).exists():
            errors.append('Username already exists')

        if not first_name:
            errors.append('First name is required')

        if not last_name:
            errors.append('Last name is required')

        if errors:
            return render(request, 'pages/user_settings.html', {
                'user': user,
                'countries': countries,
                'errors': errors
            })

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.bio = bio
        user.gender = gender if gender else None

        if country_id:
            user.country_id = country_id
        else:
            user.country_id = None

        if request.FILES.get('profile_picture'):
            user.profile_picture = request.FILES['profile_picture']

        user.save()

        return render(request, 'pages/user_settings.html', {
            'user': user,
            'countries': countries,
            'success': 'Profile updated successfully!'
        })

    return render(request, 'pages/user_settings.html', {
        'user': request.user,
        'countries': countries
    })

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()

    return redirect('app:home')

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
        'platforms': get_all_platforms(), 
        'genres': get_all_genres_from_api(), 
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
        return render(request, 'pages/main.html', status=404)


def _safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def _safe_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def _resolve_content(ctype, cid):
    """Find API content dict and local ORM object from ctype/cid."""
    from datetime import date

    data = get_all_series() if ctype == 'series' else get_all_movies()
    api_content = next(
        (item for item in data 
         if slugify(f"{item.get('title', '').replace(' ', '-')}_{item.get('year', item.get('start_year', ''))}") 
            == slugify(str(cid))),
        None
    )
    if not api_content:
        return None, None

    model_class = Series if ctype == 'series' else Movie
    local_content = model_class.objects.filter(title=api_content['title']).first()
    if local_content:
        return api_content, local_content

    defaults = {
        'synopsis': api_content.get('synopsis')  or 'No synopsis available.',
        'rating': _safe_float(api_content.get('rating')),
    }
    if ctype == 'series':
        defaults.update({
            'start_year': _safe_int(api_content.get('start_year')),
            'end_year': _safe_int(api_content.get('end_year')) if api_content.get('end_year') else None,
            'total_seasons': _safe_int(api_content.get('total_seasons')),
        })
    else:
        release_date_str = api_content.get('release_date')
        try:
            release_date = date.fromisoformat(release_date_str) if release_date_str else date.today()
        except (ValueError, TypeError):
            release_date = date.today()
        defaults.update({
            'year': _safe_int(api_content.get('year')),
            'release_date': release_date,
            'duration_minutes': _safe_int(api_content.get('duration_minutes')),
        })

    local_content = model_class.objects.create(title=api_content['title'], **defaults)
    return api_content, local_content


@login_required
def update_status(request, ctype, cid):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            status = data.get('status', 'not_seen')

            _, local_content = _resolve_content(ctype, cid)
            if not local_content:
                return JsonResponse({'success': False, 'error': 'Content not found'})

            vp, created = VisualizationProgress.objects.get_or_create(
                user=request.user,
                content=local_content
            )

            if status == 'completed':
                vp.completed = True
            elif status == 'watching':
                vp.completed = False
                vp.last_minute = vp.last_minute if vp.last_minute > 0 else 1
            else:
                vp.completed = False
                vp.last_minute = 0

            vp.save()
            return JsonResponse({'success': True, 'status': status})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid method'})


@login_required
def toggle_favorite(request, ctype, cid):
    if request.method == 'POST':
        try:
            _, local_content = _resolve_content(ctype, cid)
            if not local_content:
                return JsonResponse({'success': False, 'error': 'Content not found'})

            favorite = Favorite.objects.filter(user=request.user, content=local_content).first()
            if favorite:
                favorite.delete()
                return JsonResponse({'success': True, 'is_favorite': False})
            else:
                Favorite.objects.create(user=request.user, content=local_content)
                return JsonResponse({'success': True, 'is_favorite': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid method'})
    
@login_required
def personal_library(request):

    # HELPERS
    def build_movie_item(movie, extra=None):
        data = {
            'title': movie.title,
            'rating': movie.rating,
            'genre_name': movie.genre.name if movie.genre else 'Unknown',
            'platforms': [],
            'year': movie.year,
            'unique_id': f"{movie.title.lower().replace(' ', '-')}_{movie.year}",
        }

        if extra:
            data.update(extra)

        return data

    def build_series_item(series, extra=None):
        data = {
            'title': series.title,
            'rating': series.rating,
            'genre_name': series.genre.name if series.genre else 'Unknown',
            'platforms': [],
            'start_year': series.start_year,
            'unique_id': f"{series.title.lower().replace(' ', '-')}_{series.start_year}",
        }

        if extra:
            data.update(extra)

        return data
    
    # FAVORITES
    favorites_qs = (
        Favorite.objects
        .filter(user=request.user)
        .select_related(
            'content',
            'content__movie',
            'content__movie__genre',
            'content__series',
            'content__series__genre',
        )
    )

    favorite_movies = []
    favorite_series = []

    favorites_count = 0

    for fav in favorites_qs:
        favorites_count += 1

        content = fav.content

        if hasattr(content, 'movie'):
            favorite_movies.append(
                build_movie_item(content.movie)
            )

        elif hasattr(content, 'series'):
            favorite_series.append(
                build_series_item(content.series)
            )

    # CONTINUE WATCHING
    continue_qs = (
        VisualizationProgress.objects
        .filter(
            user=request.user,
            completed=False
        )
        .exclude(last_minute=0)
        .select_related(
            'content',
            'content__movie',
            'content__movie__genre',
            'content__series',
            'content__series__genre',
        )
    )

    continue_watching_movies = []
    continue_watching_series = []

    watching_count = 0

    for vp in continue_qs:
        watching_count += 1

        content = vp.content

        if hasattr(content, 'movie'):
            movie = content.movie


            continue_watching_movies.append(
                build_movie_item(movie, {
                    'last_minute': vp.last_minute,
                    'total_duration': movie.duration_minutes,
                })
            )

        elif hasattr(content, 'series'):
            continue_watching_series.append(
                build_series_item(content.series, {
                    'progress': 0,
                    'last_minute': vp.last_minute,
                    'total_duration': 0,
                })
            )

    # COMPLETED
    completed_qs = (
        VisualizationProgress.objects
        .filter(
            user=request.user,
            completed=True
        )
        .select_related(
            'content',
            'content__movie',
            'content__movie__genre',
            'content__series',
            'content__series__genre',
        )
    )

    completed_movies = []
    completed_series = []

    completed_count = 0

    for vp in completed_qs:
        completed_count += 1

        content = vp.content

        if hasattr(content, 'movie'):
            completed_movies.append(
                build_movie_item(content.movie)
            )

        elif hasattr(content, 'series'):
            completed_series.append(
                build_series_item(content.series)
            )

    return render(request, 'pages/personal_library.html', {
        'favorites_count': favorites_count,
        'watching_count': watching_count,
        'completed_count': completed_count,

        'favorite_movies': favorite_movies,
        'favorite_series': favorite_series,

        'continue_watching_movies': continue_watching_movies,
        'continue_watching_series': continue_watching_series,

        'completed_movies': completed_movies,
        'completed_series': completed_series,
    })


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
    
    watch_progress = VisualizationProgress.objects.filter(
        user=user,  
        completed=False
    ).select_related('content').order_by('-id')

    
    for progress in watch_progress:
        movie = Movie.objects.filter(id=progress.content.id).first()
        progress.total_duration = movie.duration_minutes if movie else 90 
        
        progress.minutes_left = max(0, progress.total_duration - progress.last_minute)
        
        catalog_entry = Catalog.objects.filter(content=progress.content).first()
        progress.platform_name = catalog_entry.platform.platform_name if catalog_entry else "StreamSync"
        
        progress.ctype = 'movie' if movie else 'series'
        progress.slug = slugify(f"{progress.content.title}_{movie.year if movie else progress.content.id}")
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

    if user.is_superuser or user.groups.filter(name='director').exists():
        return redirect('app:direction_dashboard')

    elif user.groups.filter(name='technical').exists():
        return redirect('tech_admin:index')
    
    elif user.groups.filter(name='plataform').exists():
        return redirect('app:series')  # provisional redirect

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
def tech_add_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_again')

        role_id = request.POST.get('role')
        profile_img = request.FILES.get('profile_image')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect(request.path)

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=pass1,
                first_name=first_name,
                last_name=last_name
            )

            if role_id:
                user.role = Group.objects.get(id=role_id)

            if profile_img:
                user.profile_picture = profile_img

            user.save()

            messages.success(request, f"User {username} created successfully!")
            return redirect('tech_admin:index')

        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect(request.path)

    groups = Group.objects.all()
    return render(request, 'admin/tech_add_user.html', {'groups': groups})

def tech_edit_user_view(request, user_id):
    user_to_edit = get_object_or_404(User, id=user_id)
    groups = Group.objects.all()

    if request.method == 'POST':
        user_to_edit.username = request.POST.get('username')
        user_to_edit.first_name = request.POST.get('first_name')
        user_to_edit.last_name = request.POST.get('last_name')
        user_to_edit.email = request.POST.get('email')

        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_again')
        if pass1:
            if pass1 == pass2:
                user_to_edit.set_password(pass1)
            else:
                messages.error(request, "Las contraseñas no coinciden.")
                return redirect(request.path)

        role_id = request.POST.get('role')
        profile_img = request.FILES.get('profile_image')

        if role_id:
            user_to_edit.role = Group.objects.get(id=role_id)

        if profile_img:
            user_to_edit.profile_picture = profile_img

        try:
            user_to_edit.save()
            messages.success(request, f"Usuario {user_to_edit.username} actualizado correctamente.")
            return redirect('tech_admin:index')
        except Exception as e:
            messages.error(request, f"Error al guardar: {e}")

    return render(request, 'admin/tech_edit_user.html', {
        'user_to_edit': user_to_edit,
        'groups': groups
    })

def tech_delete_user(request, user_id):
    if request.user.id == user_id:
        messages.error(request, "No puedes borrar tu propia cuenta desde aquí.")
        return redirect('tech_admin:index')

    user_to_delete = get_object_or_404(User, id=user_id)
    username = user_to_delete.username

    if request.method == 'POST':
        user_to_delete.delete()
        messages.success(request, f"Usuario {username} eliminado permanentemente.")

    return redirect('tech_admin:index')

@login_required
def direction_dashboard(request):
    if not (request.user.groups.filter(name='director').exists() or request.user.is_superuser):
        raise PermissionDenied

    stats_qs, content_qs = DashboardService.apply_filters(request.GET)

    metrics = stats_qs.aggregate(sc=Sum('total_clicks'), sf=Sum('total_favorites'))
    totals = {'clicks': metrics['sc'] or 0, 'favs': metrics['sf'] or 0}

    top_p = stats_qs.values('platform__platform_name').annotate(c=Sum('total_clicks')).order_by('-c').first()

    trending = content_qs.annotate(
        fav_count=Count('favorite')
    ).select_related('genre', 'country', 'director').order_by('-fav_count')[:10]

    if request.GET.get('export') == 'csv':
        return DashboardService.get_csv_response(trending, totals, top_p)

    chart_qs = stats_qs.values('week').annotate(c=Sum('total_clicks')).order_by('week')

    if chart_qs.exists():
        labels = [d['week'].strftime('%d %b') for d in chart_qs]
        values = [d['c'] for d in chart_qs]
    else:
        labels, values = ["No Data"], [0]

    return render(request, 'pages/direction_dashboard.html', {
        'total_clicks': f"{totals['clicks']:,}".replace(",", "."),
        'total_favorites': f"{totals['favs']:,}".replace(",", "."),
        'top_platform': top_p,
        'trending_content': trending,
        'platforms': Platform.objects.all(),
        'countries': Country.objects.all(),
        'genres': Genre.objects.all(),
        'chart_labels': json.dumps(labels),
        'chart_values': json.dumps(values),
        'filters': request.GET
    })
