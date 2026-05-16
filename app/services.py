from django.db.models import Q, Prefetch
from app.models import (
    Movie, Series, Genre, Director, 
    Platform, Catalog, AudiovisualContent
)


def get_all_platforms():
    """Retorna los nombres de las plataformas configuradas."""
    return list(Platform.objects.values_list('platform_name', flat=True))


def get_all_genres_from_api():
    """Obtiene géneros únicos desde la base de datos."""
    return list(Genre.objects.values_list('name', flat=True).order_by('name'))


def get_all_movies(platform_filter=None):
    """Obtener todas las películas desde la base de datos."""
    movies_queryset = Movie.objects.select_related(
        'genre', 'director', 'director__country', 'age_rating'
    ).prefetch_related(
        Prefetch('catalog_set', queryset=Catalog.objects.select_related('platform'))
    )
    
    movies_list = []
    
    for movie in movies_queryset:
        # Skip movies with invalid data
        if not movie.title or not movie.year:
            continue
            
        # Obtener todas las plataformas donde está disponible
        platforms = [
            catalog.platform.platform_name 
            for catalog in movie.catalog_set.all()
        ]
        
        # Filtrar por plataforma si se especifica
        if platform_filter and platform_filter not in platforms:
            continue
        
        # FIX: Ensure identifier is never empty
        identifier = f"{movie.title.lower().strip()}_{movie.year}"
        
        movie_data = {
            'id': movie.id,
            'title': movie.title,
            'synopsis': movie.synopsis or '',
            'rating': movie.rating or 0.0,
            'year': movie.year,
            'release_date': str(movie.release_date) if movie.release_date else None,
            'duration_minutes': movie.duration_minutes or 0,
            'genre_name': movie.genre.name if movie.genre else "Unknown",
            'director': movie.director.name if movie.director else "Unknown Director",
            'director_nationality': movie.director.country.name if movie.director and movie.director.country else "Unknown",
            'age_rating': str(movie.age_rating) if movie.age_rating else "NR",
            'platforms': platforms,
            'unique_id': identifier,  # This should never be empty now
            'content_type': 'movie'
        }
        
        movies_list.append(movie_data)
    
    return movies_list


def get_all_series(platform_filter=None):
    """Obtener todas las series desde la base de datos."""
    series_queryset = Series.objects.select_related(
        'genre', 'director', 'director__country', 'age_rating'
    ).prefetch_related(
        Prefetch('catalog_set', queryset=Catalog.objects.select_related('platform'))
    )
    
    series_list = []
    
    for serie in series_queryset:
        # Skip series with invalid data
        if not serie.title or not serie.start_year:
            continue
            
        # Obtener todas las plataformas donde está disponible
        platforms = [
            catalog.platform.platform_name 
            for catalog in serie.catalog_set.all()
        ]
        
        # Filtrar por plataforma si se especifica
        if platform_filter and platform_filter not in platforms:
            continue
        
        # FIX: Ensure identifier is never empty
        identifier = f"{serie.title.lower().strip()}_{serie.start_year}"
        
        serie_data = {
            'id': serie.id,
            'title': serie.title,
            'synopsis': serie.synopsis or '',
            'rating': serie.rating or 0.0,
            'start_year': serie.start_year,
            'end_year': serie.end_year,
            'total_seasons': serie.total_seasons or 1,
            'genre_name': serie.genre.name if serie.genre else "Unknown",
            'genre_description': serie.genre.description if serie.genre else "",
            'director': serie.director.name if serie.director else "Unknown Director",
            'director_nationality': serie.director.country.name if serie.director and serie.director.country else "Unknown",
            'age_rating': str(serie.age_rating) if serie.age_rating else "NR",
            'platforms': platforms,
            'unique_id': identifier,  # This should never be empty now
            'content_type': 'series'
        }
        
        series_list.append(serie_data)
    
    return series_list

def get_movies_by_genres(genre_names, min_total=5):
    """Obtiene películas agrupadas por géneros desde la base de datos."""
    all_movies = get_all_movies()
    
    result = {}
    used_movies = []
    
    # Primero: intentar 3+ de cada género
    for genre_name in genre_names:
        genre_movies = [
            m for m in all_movies 
            if m.get('genre_name', '').lower() == genre_name.lower()
        ]
        genre_movies.sort(key=lambda x: x.get('rating', 0), reverse=True)
        
        selected = []
        for m in genre_movies:
            if m['unique_id'] not in [um['unique_id'] for um in used_movies]:
                selected.append(m)
                used_movies.append(m)
                if len(selected) >= 3:
                    break
        
        result[genre_name] = selected
    
    # Contar total actual
    current_total = sum(len(movies) for movies in result.values())
    
    # Si no llega a min_total, completar con otros géneros
    if current_total < min_total:
        remaining = min_total - current_total
        extra_movies = []
        for m in all_movies:
            if m['unique_id'] not in [um['unique_id'] for um in used_movies] and len(extra_movies) < remaining:
                extra_movies.append(m)
        
        genre_list = list(result.keys())
        idx = 0
        for m in extra_movies:
            while len(result[genre_list[idx]]) >= 5 and idx < len(genre_list) - 1:
                idx += 1
            if idx < len(genre_list):
                result[genre_list[idx]].append(m)
    
    return result


def get_series_by_genres(genre_names, min_total=5):
    """Obtiene series agrupadas por géneros desde la base de datos."""
    all_series = get_all_series()
    
    result = {}
    used_series = []
    
    for genre_name in genre_names:
        genre_series = [
            s for s in all_series 
            if s.get('genre_name', '').lower() == genre_name.lower()
        ]
        genre_series.sort(key=lambda x: x.get('rating', 0), reverse=True)
        
        selected = []
        for s in genre_series:
            if s['unique_id'] not in [us['unique_id'] for us in used_series]:
                selected.append(s)
                used_series.append(s)
                if len(selected) >= 3:
                    break
        
        result[genre_name] = selected
    
    current_total = sum(len(series_list) for series_list in result.values())
    
    if current_total < min_total:
        remaining = min_total - current_total
        extra_series = []
        for s in all_series:
            if s['unique_id'] not in [us['unique_id'] for us in used_series] and len(extra_series) < remaining:
                extra_series.append(s)
        
        genre_list = list(result.keys())
        idx = 0
        for s in extra_series:
            while len(result[genre_list[idx]]) >= 5 and idx < len(genre_list) - 1:
                idx += 1
            if idx < len(genre_list):
                result[genre_list[idx]].append(s)
    
    return result


def get_trending(limit=10):
    """
    Obtiene las películas y series mejor valoradas (Top Rated) desde la DB.
    """
    all_movies = get_all_movies()
    all_series = get_all_series()
    
    all_content = all_movies + all_series
    all_content.sort(key=lambda x: x.get('rating', 0), reverse=True)
    
    return all_content[:limit]


def search_content(query, platform=None, genre=None, sort_rating=None, sort_year=None):
    """Busca contenido en la base de datos."""
    results = []
    
    # Buscar películas
    movies_q = Q(title__icontains=query)
    if genre:
        movies_q &= Q(genre__name__icontains=genre)
    
    movies = Movie.objects.filter(movies_q).select_related(
        'genre', 'director', 'age_rating'
    ).prefetch_related(
        Prefetch('catalog_set', queryset=Catalog.objects.select_related('platform'))
    )
    
    for movie in movies:
        platforms = [catalog.platform.platform_name for catalog in movie.catalog_set.all()]
        
        # Filtrar por plataforma
        if platform and platform not in platforms:
            continue
        
        identifier = f"{movie.title}_{movie.year}".lower().strip()
        
        results.append({
            'id': movie.id,
            'title': movie.title,
            'synopsis': movie.synopsis,
            'rating': movie.rating,
            'year': movie.year,
            'genre_name': movie.genre.name if movie.genre else "Unknown",
            'platforms': platforms,
            'unique_id': identifier,
            'content_type': 'movie'
        })
    
    # Buscar series
    series_q = Q(title__icontains=query)
    if genre:
        series_q &= Q(genre__name__icontains=genre)
    
    series = Series.objects.filter(series_q).select_related(
        'genre', 'director', 'age_rating'
    ).prefetch_related(
        Prefetch('catalog_set', queryset=Catalog.objects.select_related('platform'))
    )
    
    for serie in series:
        platforms = [catalog.platform.platform_name for catalog in serie.catalog_set.all()]
        
        if platform and platform not in platforms:
            continue
        
        identifier = f"{serie.title}_{serie.start_year}".lower().strip()
        
        results.append({
            'id': serie.id,
            'title': serie.title,
            'synopsis': serie.synopsis,
            'rating': serie.rating,
            'start_year': serie.start_year,
            'genre_name': serie.genre.name if serie.genre else "Unknown",
            'platforms': platforms,
            'unique_id': identifier,
            'content_type': 'series'
        })
    
    # Ordenar resultados
    if sort_rating:
        results.sort(key=lambda x: x.get('rating', 0), reverse=(sort_rating == 'desc'))
    elif sort_year:
        results.sort(
            key=lambda x: x.get('year') or x.get('start_year', 0), 
            reverse=(sort_year == 'desc')
        )
    
    return results