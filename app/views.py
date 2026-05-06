from django.contrib.auth.forms import UserCreationForm
from .services import get_all_movies, get_all_series, search_content
from django.shortcuts import render, redirect
from django.db.models import Sum, Count
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .models import *
from .utils import DashboardService

import json

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



def main(request):
    return render(request, 'pages/main.html')

@login_required
def login_redirect(request):
    user = request.user

    if user.is_superuser or user.groups.filter(name='director').exists():
        return redirect('app:direction_dashboard')

    elif user.groups.filter(name='technical').exists():
        return redirect('app:series') #provisional redirect
    
    elif user.groups.filter(name='plataform').exists():
        return redirect('app:series') #provisional redirect

    else:
        return redirect('app:main')


@login_required
def direction_dashboard(request):
    if request.user.groups.filter(name='director').exists() and not request.user.is_superuser:
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