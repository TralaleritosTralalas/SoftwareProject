import requests
from django.urls import reverse
from decouple import config

TMDB_API_KEY = config("TMDB_API_KEY")
TMDB_ACCESS_TOKEN = config("TMDB_ACCESS_TOKEN")
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w300"

_tmdb_cache = {}

def get_tmdb_data(title, year=None, content_type="movie"):
    """
    Busca en TMDB por título y año y retorna un dict con:
    - poster_url: URL del póster
    - overview: synopsis/descripción
    """
    cache_key = f"{title}_{year}_{content_type}"
    if cache_key in _tmdb_cache:
        return _tmdb_cache[cache_key]

    try:
        search_url = "https://api.themoviedb.org/3/search/movie" if content_type == "movie" else "https://api.themoviedb.org/3/search/tv"
        params = {
            "api_key": TMDB_API_KEY,
            "query": title,
        }
        if year:
            if content_type == "movie":
                params["year"] = year
            else:
                params["first_air_date_year"] = year

        headers = {"Authorization": f"Bearer {TMDB_ACCESS_TOKEN}"}
        response = requests.get(search_url, params=params, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("results"):
                result = data["results"][0]
                poster_path = result.get("poster_path")
                poster_url = f"{TMDB_IMAGE_BASE_URL}{poster_path}" if poster_path else None
                overview = result.get("overview")

                tmdb_data = {
                    "poster_url": poster_url,
                    "overview": overview
                }
                _tmdb_cache[cache_key] = tmdb_data
                return tmdb_data
    except Exception:
        pass

    _tmdb_cache[cache_key] = None
    return None


def get_tmdb_poster(title, year=None, content_type="movie"):
    """
    Busca el póster de TMDB por título y año.
    Retorna la URL del póster o None si no se encuentra.
    """
    tmdb_data = get_tmdb_data(title, year, content_type)
    return tmdb_data.get("poster_url") if tmdb_data else None

# URL DE LAS MOVIES-API EN LOCAL
url_local_1 = "http://127.0.0.1:8080" #API LOCAL 1
url_local_2 = "http://127.0.0.1:8081" #API LOCAL 2
url_local_3 = "http://127.0.0.1:8082" #API LOCAL 3
     
# API KEYS DE LAS MOVIES-API EN LOCAL
api_key_local_1 = config("API_KEY_LOCAL_1")
api_key_local_2 = config("API_KEY_LOCAL_2")
api_key_local_3 = config("API_KEY_LOCAL_3")

#PLATAFORMAS
PLATFORMS = [
    (url_local_1, api_key_local_1, "Platform 1"),
    (url_local_2, api_key_local_2, "Platform 2"),
    (url_local_3, api_key_local_3, "Platform 3"),
]


def get_local_movies(url, api_key): #de una "plataforma" obtengo sus peliculas
    try:
        response = requests.get(
            f"{url}/movies", 
            headers={"X-API-KEY": api_key},
            timeout=5
        )
        response.raise_for_status() 
        print(response.status_code, response.text)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return []

def get_local_series(url, api_key): #de una "plataforma" obtengo sus series
    try:
        response = requests.get(
            f"{url}/series", 
            headers={"X-API-KEY": api_key},
            timeout=5
        )
        response.raise_for_status() 
        print(response.status_code, response.text)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return []

def get_genre(url, api_key):
    try:
        response = requests.get(
            f"{url}/genres", 
            headers={"X-API-KEY": api_key}, 
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return []
    
def get_directors(url, api_key):
    try:
        response = requests.get(
            f"{url}/directors", 
            headers={"X-API-KEY": api_key}, 
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return []

def get_all_platforms():
    """Retorna los nombres de las plataformas configuradas."""
    return [p[2] for p in PLATFORMS]

def get_all_genres_from_api():
    """Obtiene géneros únicos consultando todas las APIs configuradas."""
    all_genres = set()
    for url, key, _ in PLATFORMS:
        genres = get_genre(url, key)
        for g in genres:
            all_genres.add(g["name"])
    return sorted(list(all_genres))

def get_all_movies(platform_filter= None):  # obtener todas las peliculas de todas las "plataformas"

    movies_dict = {} #diccionario para saber el contenido

    for url, key, platform_name in PLATFORMS:
        if platform_filter and platform_name != platform_filter:
            continue
        
        # mapa de generos x plataforma
        genre_map = {}
        director_map = {}

        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        directors = get_directors(url, key)
        for d in directors:
            director_map[d["id"]] = {
                "name": d.get("name", "Unknown Director"),
                "nationality": d.get("country", {}).get("name") if isinstance(d.get("country"), dict) else "Unknown"
            }

        movies = get_local_movies(url, key)
        for movie in movies:
            identifier = f"{movie.get('title')}_{movie.get('year')}".lower().strip() #identificador del contenido
            
            if identifier not in movies_dict:
                # TMDB data
                tmdb_data = get_tmdb_data(movie.get('title'), movie.get('year'), "movie")
                movie["poster_url"] = tmdb_data.get("poster_url") if tmdb_data else None

                # Género y descripción
                movie["genre_name"] = genre_map.get(movie.get('genre_id'), "Unknown")
                dir_info = director_map.get(movie.get("director_id"), {})
                movie["director"] = dir_info.get("name", "Unknown Director")
                movie["director_nationality"] = dir_info.get("nationality", "Unknown")

                # Completar synopsis desde TMDB si no existe
                local_synopsis = movie.get("synopsis", "")
                if not local_synopsis or local_synopsis.lower() in ["", "no synopsis available."]:
                    if tmdb_data and tmdb_data.get("overview"):
                        movie["synopsis"] = tmdb_data["overview"]

                # Otros datos
                movie["age_rating"] = movie.get("age_rating", {}).get("title", "NR")
                movie["duration_minutes"] = movie.get("duration_minutes", "—")
                movie['unique_id'] = identifier

                movie["platforms"] = [platform_name]
                movie.pop("platform_name", None)
                movies_dict[identifier] = movie
                print(f"DEBUG MOVIE DATA: {movie}")
                
            else:
                if platform_name not in movies_dict[identifier]["platforms"]:
                    movies_dict[identifier]["platforms"].append(platform_name)
    return list(movies_dict.values())


def get_all_series(platform_filter = None):  # obtener todas las peliculas de todas las "plataformas"
    series_dict = {}

    for url, key, platform_name in PLATFORMS:
        if platform_filter and platform_name != platform_filter:
            continue
        genre_map = {}
        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        series = get_local_series(url, key)

        for serie in series:
            identifier = f"{serie.get('title')}_{serie.get('start_year', '')}".lower().strip()

            if identifier not in series_dict:
                # TMDB data
                tmdb_data = get_tmdb_data(serie.get('title'), serie.get('start_year'), "tv")
                serie["poster_url"] = tmdb_data.get("poster_url") if tmdb_data else None

                serie["genre_name"] = serie.get("genre", {}).get("name") or genre_map.get(serie.get("genre_id"), "Unknown")
                serie["synopsis"] = serie.get("synopsis", "No synopsis available.")

                # Completar synopsis desde TMDB si no existe
                local_synopsis = serie.get("synopsis", "")
                if not local_synopsis or local_synopsis.lower() in ["", "no synopsis available."]:
                    if tmdb_data and tmdb_data.get("overview"):
                        serie["synopsis"] = tmdb_data["overview"]

                director_data = serie.get("director", {})
                serie["director"] = director_data.get("name", "Unknown Director")

                serie["director_nationality"] = director_data.get("country", {}).get("name", "Unknown")
                serie["genre_description"] = serie.get("genre", {}).get("description", "")
                serie["age_rating"] = serie.get("age_rating", {}).get("title", "NR")
                serie['unique_id'] = identifier

                serie["platforms"] = [platform_name]
                serie.pop("platform_name", None)
                series_dict[identifier] = serie
            else:
                if platform_name not in series_dict[identifier]["platforms"]:
                    series_dict[identifier]["platforms"].append(platform_name)
    
    return list(series_dict.values())


def get_movies_by_genres(genre_names, min_total=5):
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
        
        # Tomar hasta 3 películas de este género
        selected = []
        for m in genre_movies:
            if m not in used_movies:
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
        # Recolectar movies adicionales de otros géneros
        extra_movies = []
        for m in all_movies:
            if m not in used_movies and len(extra_movies) < remaining:
                extra_movies.append(m)
        
        # Distribuir los extras entre los géneros
        genre_list = list(result.keys())
        idx = 0
        for m in extra_movies:
            while len(result[genre_list[idx]]) >= 5 and idx < len(genre_list) - 1:
                idx += 1
            if idx < len(genre_list):
                m_copy = m.copy()
                m_copy['unique_id'] = f"{m.get('title', '').lower().replace(' ', '-')}_{m.get('year', '')}"
                result[genre_list[idx]].append(m_copy)
    
    # Asignar unique_id a cada movie que no lo tenga
    for genre_name, movies in result.items():
        for m in movies:
            if 'unique_id' not in m:
                m['unique_id'] = f"{m.get('title', '').lower().replace(' ', '-')}_{m.get('year', '')}"
    
    return result


def get_series_by_genres(genre_names, min_total=5):
    all_series = get_all_series()
    
    result = {}
    used_series = []
    
    # Primero: intentar 3+ de cada género
    for genre_name in genre_names:
        genre_series = [
            s for s in all_series 
            if s.get('genre_name', '').lower() == genre_name.lower()
        ]
        genre_series.sort(key=lambda x: x.get('rating', 0), reverse=True)
        
        # Tomar hasta 3 series de este género
        selected = []
        for s in genre_series:
            if s not in used_series:
                selected.append(s)
                used_series.append(s)
                if len(selected) >= 3:
                    break
        
        result[genre_name] = selected
    
    # Contar total actual
    current_total = sum(len(series_list) for series_list in result.values())
    
    # Si no llega a min_total, completar con otros géneros
    if current_total < min_total:
        remaining = min_total - current_total
        # Recolectar series adicionales de otros géneros
        extra_series = []
        for s in all_series:
            if s not in used_series and len(extra_series) < remaining:
                extra_series.append(s)
        
        # Distribuir los extras entre los géneros
        genre_list = list(result.keys())
        idx = 0
        for s in extra_series:
            while len(result[genre_list[idx]]) >= 5 and idx < len(genre_list) - 1:
                idx += 1
            if idx < len(genre_list):
                s_copy = s.copy()
                s_copy['unique_id'] = f"{s.get('title', '').lower().replace(' ', '-')}_{s.get('start_year', '')}"
                result[genre_list[idx]].append(s_copy)
    
    # Asignar unique_id a cada serie que no lo tenga
    for genre_name, series_list in result.items():
        for s in series_list:
            if 'unique_id' not in s:
                s['unique_id'] = f"{s.get('title', '').lower().replace(' ', '-')}_{s.get('start_year', '')}"
    
    return result


def get_trending(limit=10):
    """
    Obtiene las películas y series mejor valoradas (Top Rated).
    Combina movies y series, ordena por rating descendente.
    """
    all_movies = get_all_movies()
    all_series = get_all_series()
    
    all_content = []
    
    for m in all_movies:
        m['content_type'] = 'movie'
        m['unique_id'] = f"{m.get('title', '').lower().replace(' ', '-')}_{m.get('year', '')}"
        all_content.append(m)
    
    for s in all_series:
        s['content_type'] = 'series'
        s['unique_id'] = f"{s.get('title', '').lower().replace(' ', '-')}_{s.get('start_year', '')}"
        all_content.append(s)
    
    all_content.sort(key=lambda x: x.get('rating', 0), reverse=True)
    
    return all_content[:limit]


def search_content(query, platform=None, genre=None, sort_rating=None, sort_year=None):
    results_dict = {}

    for url, key, platform_name in PLATFORMS:
        if platform and platform_name != platform:
            continue

        genre_map = {g["id"]: g["name"] for g in get_genre(url, key)}

        # --- Búsqueda en Películas ---
        try:
            res = requests.get(f"{url}/movies", headers={"X-API-KEY": key}, params={"title": query}, timeout=5)
            if res.status_code == 200:
                for movie in res.json():
                    movie_genre = genre_map.get(movie.get("genre_id"), "Unknown")
                    if genre and genre.lower() not in movie_genre.lower():
                        continue
                    
                    clean_title = movie.get('title', '').lower().strip()
                    year = movie.get('year', '')
                    identifier = f"{clean_title}_{year}" 
                    
                    if identifier not in results_dict:
                        tmdb_data = get_tmdb_data(movie.get('title'), movie.get('year'), "movie")
                        movie["poster_url"] = tmdb_data.get("poster_url") if tmdb_data else None
                        movie["content_type"] = "movie"
                        movie["genre_name"] = movie_genre
                        movie["platforms"] = [platform_name]
                        movie["unique_id"] = identifier  
                        results_dict[identifier] = movie
                    else:
                        if platform_name not in results_dict[identifier]["platforms"]:
                            results_dict[identifier]["platforms"].append(platform_name)
        except:
            pass

        # --- Búsqueda en Series ---
        try:
            res = requests.get(f"{url}/series", headers={"X-API-KEY": key}, params={"title": query}, timeout=5)
            if res.status_code == 200:
                for serie in res.json():
                    serie_genre = genre_map.get(serie.get("genre_id"), "Unknown")
                    if genre and genre.lower() not in serie_genre.lower():
                        continue
                    
                    # CAMBIO AQUÍ: Eliminamos el prefijo 'series_'
                    clean_title = serie.get('title', '').lower().strip()
                    year = serie.get('start_year', '')
                    identifier = f"{clean_title}_{year}"
                    
                    if identifier not in results_dict:
                        tmdb_data = get_tmdb_data(movie.get('title'), movie.get('year'), "movie")
                        movie["poster_url"] = tmdb_data.get("poster_url") if tmdb_data else None
                        serie["content_type"] = "series"
                        serie["genre_name"] = serie_genre
                        serie["platforms"] = [platform_name]
                        serie["unique_id"] = identifier
                        results_dict[identifier] = serie
                    else:
                        if platform_name not in results_dict[identifier]["platforms"]:
                            results_dict[identifier]["platforms"].append(platform_name)
        except:
            pass

    # ... (resto de la lógica de ordenación y retorno)
    return list(results_dict.values())