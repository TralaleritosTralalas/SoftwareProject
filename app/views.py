from django.contrib.auth.forms import UserCreationForm
from .services import get_all_movies, get_all_series, get_movies_by_genres, get_series_by_genres, \
    get_trending, get_all_platforms, get_all_genres_from_api, search_content
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.utils.text import slugify
from app.models import User, Country
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


def catalog(request):
    selected_platform = request.GET.get('platform')
    selected_genre = request.GET.get('genre')
    sort_rating = request.GET.get('sort_rating')
    sort_year = request.GET.get('sort_year')

    movies = get_all_movies(platform_filter=selected_platform)
    series = get_all_series(platform_filter=selected_platform)

    if selected_genre:
        movies = [m for m in movies if m.get('genre_name') == selected_genre]
        series = [s for s in series if s.get('genre_name') == selected_genre]

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

    if selected_genre:
        movies_list = [m for m in movies_list if m.get('genre_name') == selected_genre]

    if sort_rating:
        movies_list.sort(key=lambda x: x.get('rating', 0), reverse=(sort_rating == 'desc'))
    if sort_year:
        movies_list.sort(key=lambda x: x.get('year', 0), reverse=(sort_year == 'desc'))

    context = {
        'movies': movies_list,
        'platforms': get_all_platforms(),
        'genres': get_all_genres_from_api(),
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

    if selected_genre:
        series_list = [s for s in series_list if s.get('genre_name') == selected_genre]

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
    return render(request, 'streamsync_register.html', {
        'form': UserCreationForm
    })


def login(request):
    return render(request, 'login.html')


def content_detail(request, ctype, cid):
    from .models import VisualizationProgress, Favorite, Watchlist
    
    if ctype == 'series':
        data = get_all_series()
    else:
        data = get_all_movies()

    content = next((item for item in data if slugify(
        f"{item.get('title', '').replace(' ', '-')}_{item.get('year', item.get('start_year', ''))}") == slugify(
        str(cid))), None)

    if content:
        content['content_type'] = ctype

        user_status = 'not_seen'
        is_favorite = False
        is_in_watchlist = False
        
        if request.user.is_authenticated:
            from app.models import AudiovisualContent, Movie, Series
            try:
                if ctype == 'series':
                    local_content = Series.objects.filter(title=content.get('title')).first()
                else:
                    local_content = Movie.objects.filter(title=content.get('title')).first()
                
                if local_content:
                    vp = VisualizationProgress.objects.filter(user=request.user, content=local_content).first()
                    if vp:
                        if vp.completed:
                            user_status = 'completed'
                        elif vp.last_minute > 0:
                            user_status = 'watching'

                    is_favorite = Favorite.objects.filter(user=request.user, content=local_content).exists()
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


@login_required
def update_status(request, ctype, cid):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            status = data.get('status', 'not_seen')
            
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
                elif status == 'watching':
                    vp.completed = False
                    vp.last_minute = vp.last_minute if vp.last_minute > 0 else 1
                else:
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

    if request.method == 'POST':
        try:
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

    if user.is_superuser or user.groups.filter(name='director').exists():
        return redirect('app:direction_dashboard')

    elif user.groups.filter(name='technical').exists():
        return redirect('tech_admin:index')

    elif user.groups.filter(name='manager').exists():
        return redirect('app:manager_dashboard')

    if not user.onboarding_completed:
        return redirect('app:onboarding')

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

    # --- Trend chart (clicks over time) ---
    chart_qs = stats_qs.values('week').annotate(c=Sum('total_clicks')).order_by('week')
    labels = [d['week'].strftime('%d %b') for d in chart_qs] if chart_qs.exists() else ["No Data"]
    values = [d['c'] for d in chart_qs] if chart_qs.exists() else [0]

    # --- Genre distribution (bar chart) ---
    genre_qs = content_qs.values('genre__name').annotate(cnt=Count('id')).order_by('-cnt')[:8]
    genre_labels = [g['genre__name'] or 'Unknown' for g in genre_qs] if genre_qs.exists() else ["No Data"]
    genre_values = [g['cnt'] for g in genre_qs] if genre_qs.exists() else [0]

    # --- Clicks vs Favorites (doughnut) ---
    donut_labels = ['Clicks', 'Favorites']
    donut_values = [totals['clicks'], totals['favs']]

    # --- Platform comparison (grouped bar chart) ---
    platform_qs = stats_qs.values('platform__platform_name').annotate(
        total_c=Sum('total_clicks'),
        total_f=Sum('total_favorites')
    ).order_by('-total_c')[:6]

    if platform_qs.exists():
        platform_labels = [p['platform__platform_name'] for p in platform_qs]
        platform_clicks = [p['total_c'] or 0 for p in platform_qs]
        platform_favs = [p['total_f'] or 0 for p in platform_qs]
    else:
        platform_labels = ["No Data"]
        platform_clicks = [0]
        platform_favs = [0]

    # --- Top content horizontal bar ---
    top_content_labels = [c.title for c in trending] if trending.exists() else ["No Data"]
    top_content_values = [c.fav_count for c in trending] if trending.exists() else [0]

    # Mapeo limpio de filtros para los selects del Sidebar
    filters_data = {
        'range': request.GET.get('range', ''),
        'start_date': request.GET.get('start_date', ''),
        'end_date': request.GET.get('end_date', ''),
        'platform': request.GET.get('platform', 'all'),
        'country': request.GET.get('country', 'all'),
        'genre': request.GET.get('genre', 'all'),
    }

    return render(request, 'pages/direction_dashboard.html', {
        'total_clicks': f"{totals['clicks']:,}".replace(",", "."),
        'total_favorites': f"{totals['favs']:,}".replace(",", "."),
        'top_platform': top_p,
        'trending_content': trending,
        'platforms': Platform.objects.all(),
        'countries': Country.objects.all(),
        'genres': Genre.objects.all(),
        # Trend chart
        'chart_labels': json.dumps(labels),
        'chart_values': json.dumps(values),
        # Genre bar chart
        'genre_labels': json.dumps(genre_labels),
        'genre_values': json.dumps(genre_values),
        # Doughnut
        'donut_labels': json.dumps(donut_labels),
        'donut_values': json.dumps(donut_values),
        # Platform bar
        'platform_labels': json.dumps(platform_labels),
        'platform_clicks': json.dumps(platform_clicks),
        'platform_favs': json.dumps(platform_favs),
        # Top content bar
        'top_content_labels': json.dumps(top_content_labels),
        'top_content_values': json.dumps(top_content_values),
        'filters': filters_data
    })


@login_required
def manager_dashboard(request):
    # Se obtiene la plataforma asignada al Manager actual (según campo p_manager en tu modelo Platform)
    platform = Platform.objects.filter(p_manager=request.user).first()

    if not platform:
        raise PermissionDenied("You don't have a platform to manage.")

    stats_qs, content_qs = DashboardService.apply_filters(request.GET, platform=platform)

    metrics = stats_qs.aggregate(sc=Sum('total_clicks'), sf=Sum('total_favorites'))
    totals = {'clicks': metrics['sc'] or 0, 'favs': metrics['sf'] or 0}

    trending = content_qs.annotate(
        fav_count=Count('favorite')
    ).select_related('genre', 'country', 'director').order_by('-fav_count')[:10]

    if request.GET.get('export') == 'csv':
        return DashboardService.get_csv_response(trending, totals, None)

    # --- Trend chart (clicks over time) ---
    chart_qs = stats_qs.values('week').annotate(c=Sum('total_clicks')).order_by('week')
    labels = [d['week'].strftime('%d %b') for d in chart_qs] if chart_qs.exists() else ["No Data"]
    values = [d['c'] for d in chart_qs] if chart_qs.exists() else [0]

    # --- Genre distribution (bar chart) ---
    genre_qs = content_qs.values('genre__name').annotate(cnt=Count('id')).order_by('-cnt')[:8]
    genre_labels = [g['genre__name'] or 'Unknown' for g in genre_qs] if genre_qs.exists() else ["No Data"]
    genre_values = [g['cnt'] for g in genre_qs] if genre_qs.exists() else [0]

    # --- Clicks vs Favorites (doughnut) ---
    donut_labels = ['Clicks', 'Favorites']
    donut_values = [totals['clicks'], totals['favs']]

    # --- Top content horizontal bar ---
    top_content_labels = [c.title for c in trending] if trending.exists() else ["No Data"]
    top_content_values = [c.fav_count for c in trending] if trending.exists() else [0]

    # Mapeo de filtros para persistencia de búsqueda en Manager
    filters_data = {
        'range': request.GET.get('range', ''),
        'start_date': request.GET.get('start_date', ''),
        'end_date': request.GET.get('end_date', ''),
        'country': request.GET.get('country', 'all'),
        'genre': request.GET.get('genre', 'all'),
    }

    return render(request, 'pages/manager_dashboard.html', {
        'platform': platform,
        'total_clicks': f"{totals['clicks']:,}".replace(",", "."),
        'total_favorites': f"{totals['favs']:,}".replace(",", "."),
        'trending_content': trending,
        'genres': Genre.objects.all(),
        'countries': Country.objects.all(),
        # Trend chart
        'chart_labels': json.dumps(labels),
        'chart_values': json.dumps(values),
        # Genre bar chart
        'genre_labels': json.dumps(genre_labels),
        'genre_values': json.dumps(genre_values),
        # Doughnut
        'donut_labels': json.dumps(donut_labels),
        'donut_values': json.dumps(donut_values),
        # Top content bar
        'top_content_labels': json.dumps(top_content_labels),
        'top_content_values': json.dumps(top_content_values),
        'filters': filters_data
    })