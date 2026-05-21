from django.db.models import Q, Prefetch
from app.models import (
    Movie, Series, Genre, Platform, Catalog
)
import requests
from django.urls import reverse
from decouple import config
from thefuzz import fuzz


def get_all_platforms():
    return list(Platform.objects.values_list('platform_name', flat=True))


def get_all_genres_from_api():
    return list(Genre.objects.values_list('name', flat=True).order_by('name'))


def get_all_movies(platform_filter=None):
    movies_queryset = Movie.objects.select_related(
        'genre', 'director', 'director__country', 'age_rating'
    ).prefetch_related(
        Prefetch('catalog_set', queryset=Catalog.objects.select_related('platform'))
    )

    movies_list = []

    for movie in movies_queryset:
        if not movie.title or not movie.year:
            continue

        platforms = [
            catalog.platform.platform_name
            for catalog in movie.catalog_set.all()
        ]
        platforms_data = [
            {'name': catalog.platform.platform_name, 'state': catalog.state}
            for catalog in movie.catalog_set.all()
        ]
        is_unavailable = all(p['state'] == 'unavailable' for p in platforms_data) if platforms_data else False
        
        if platform_filter and platform_filter not in platforms:
            continue

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
            'platforms_data': platforms_data,
            'is_unavailable': is_unavailable,
            'poster_url': movie.poster_url or '',
            'backdrop_url': movie.backdrop_url or '',
            'unique_id': identifier,
            'content_type': 'movie'
        }

        movies_list.append(movie_data)

    return movies_list


def get_all_series(platform_filter=None):
    series_queryset = Series.objects.select_related(
        'genre', 'director', 'director__country', 'age_rating'
    ).prefetch_related(
        Prefetch('catalog_set', queryset=Catalog.objects.select_related('platform'))
    )

    series_list = []

    for serie in series_queryset:
        if not serie.title or not serie.start_year:
            continue

        platforms = [
            catalog.platform.platform_name
            for catalog in serie.catalog_set.all()
        ]
        platforms_data = [
            {'name': catalog.platform.platform_name, 'state': catalog.state}
            for catalog in serie.catalog_set.all()
        ]
        is_unavailable = all(p['state'] == 'unavailable' for p in platforms_data) if platforms_data else False
        
        if platform_filter and platform_filter not in platforms:
            continue

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
            'platforms_data': platforms_data,
            'is_unavailable': is_unavailable,
            'poster_url': serie.poster_url or '',
            'backdrop_url': serie.backdrop_url or '',
            'unique_id': identifier,
            'content_type': 'series'
        }

        series_list.append(serie_data)

    return series_list


def get_movies_by_genres(genre_names, min_total=5):
    all_movies = get_all_movies()

    result = {}
    used_movies = []

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

    current_total = sum(len(movies) for movies in result.values())

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
    all_movies = get_all_movies()
    all_series = get_all_series()

    all_content = all_movies + all_series
    all_content.sort(key=lambda x: x.get('rating', 0), reverse=True)

    return all_content[:limit]


def search_content(query, platform=None, genre=None, sort_rating=None, sort_year=None):
    results_dict = {}
    search_query = query.lower().strip()
    THRESHOLD = 60

    platform_filter = Q()
    if platform:
        platform_filter = Q(catalog__platform__platform_name=platform)

    genre_filter = Q()
    if genre:
        genre_filter = Q(genre__name__icontains=genre)

    try:
        movies = Movie.objects.select_related('genre', 'director').prefetch_related('catalog_set__platform').filter(
            platform_filter & genre_filter
        ).distinct()

        for movie in movies:
            m_title = movie.title.lower()
            d_name = movie.director.name.lower() if movie.director else "unknown director"

            score_title = fuzz.partial_ratio(search_query, m_title)
            score_director = fuzz.partial_ratio(search_query, d_name)

            if search_query not in m_title and search_query not in d_name and score_title < THRESHOLD and score_director < THRESHOLD:
                continue

            identifier = f"{m_title}_{movie.year}".strip()

            platforms_list = [cat.platform.platform_name for cat in movie.catalog_set.all()]

            if identifier not in results_dict:
                results_dict[identifier] = {
                    "id": movie.id,
                    "title": movie.title,
                    "synopsis": movie.synopsis,
                    "rating": movie.rating,
                    "year": movie.year,
                    "release_date": str(movie.release_date),
                    "duration_minutes": movie.duration_minutes,
                    "content_type": "movie",
                    "genre_name": movie.genre.name if movie.genre else "Unknown",
                    "genre_id": movie.genre.id if movie.genre else None,
                    "director": movie.director.name if movie.director else "Unknown Director",
                    "director_id": movie.director.id if movie.director else None,
                    "platforms": platforms_list,
                    'poster_url': movie.poster_url or '',
                    'backdrop_url': movie.backdrop_url or '',
                    "unique_id": identifier,
                    "search_score": max(score_title, score_director)
                }
            else:
                for p in platforms_list:
                    if p not in results_dict[identifier]["platforms"]:
                        results_dict[identifier]["platforms"].append(p)
    except Exception as e:
        print(f"Error en búsqueda de películas: {e}")

    try:
        series = Series.objects.select_related('genre', 'director').prefetch_related('catalog_set__platform').filter(
            platform_filter & genre_filter
        ).distinct()

        for serie in series:
            s_title = serie.title.lower()
            s_dir_name = serie.director.name.lower() if serie.director else "unknown director"

            score_title = fuzz.partial_ratio(search_query, s_title)
            score_director = fuzz.partial_ratio(search_query, s_dir_name)

            if search_query not in s_title and search_query not in s_dir_name and score_title < THRESHOLD and score_director < THRESHOLD:
                continue

            identifier = f"{s_title}_{serie.start_year}".strip()

            platforms_list = [cat.platform.platform_name for cat in serie.catalog_set.all()]

            if identifier not in results_dict:
                results_dict[identifier] = {
                    "id": serie.id,
                    "title": serie.title,
                    "synopsis": serie.synopsis,
                    "rating": serie.rating,
                    "start_year": serie.start_year,
                    "end_year": serie.end_year,
                    "total_seasons": serie.total_seasons,
                    "content_type": "series",
                    "genre_name": serie.genre.name if serie.genre else "Unknown",
                    "genre_id": serie.genre.id if serie.genre else None,
                    "director": serie.director.name if serie.director else "Unknown Director",
                    "director_id": serie.director.id if serie.director else None,
                    "platforms": platforms_list,
                    "unique_id": identifier,
                    "search_score": max(score_title, score_director),
                    "poster_url": serie.poster_url or '',
                    "backdrop_url": serie.backdrop_url or ''
                }
            else:

                for p in platforms_list:
                    if p not in results_dict[identifier]["platforms"]:
                        results_dict[identifier]["platforms"].append(p)
    except Exception as e:
        print(f"Error en búsqueda de series: {e}")

    final_results = list(results_dict.values())

    final_results.sort(key=lambda x: (
        not x.get('title', '').lower().startswith(search_query),
        -x.get('search_score', 0),
        x.get('title', '').lower()
    ))

    return final_results
