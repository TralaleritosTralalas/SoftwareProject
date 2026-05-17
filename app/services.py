import requests
from django.urls import reverse
from decouple import config
from thefuzz import fuzz

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
                # Género y descripción
                movie["genre_name"] = genre_map.get(movie.get('genre_id'), "Unknown")
                dir_info = director_map.get(movie.get("director_id"), {})
                movie["director"] = dir_info.get("name", "Unknown Director")
                movie["director_nationality"] = dir_info.get("nationality", "Unknown")

                # Otros datos
                movie["age_rating"] = movie.get("age_rating", {}).get("title", "NR")
                movie["duration_minutes"] = movie.get("duration_minutes", "—")
                movie['unique_id'] = identifier

                movie["platforms"] = [platform_name]
                movie.pop("platform_name", None)
                movies_dict[identifier] = movie
                
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
                serie["genre_name"] = serie.get("genre", {}).get("name") or genre_map.get(serie.get("genre_id"), "Unknown")
                serie["synopsis"] = serie.get("synopsis", "No synopsis available.")

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
    search_query = query.lower().strip()
    THRESHOLD = 60

    for url, key, platform_name in PLATFORMS:
        if platform and platform_name != platform:
            continue

        # 1. PREPARAR MAPAS (Necesarios para traducir IDs a nombres)
        genre_map = {g["id"]: g["name"] for g in get_genre(url, key)}
        # Obtenemos los directores para esta plataforma específica
        directors_data = get_directors(url, key)
        director_map = {d["id"]: d.get("name", "Unknown Director") for d in directors_data}

        # --- Búsqueda en Películas ---
        try:
            res = requests.get(f"{url}/movies", headers={"X-API-KEY": key}, timeout=5)
            if res.status_code == 200:
                for movie in res.json():
                    # Obtener nombre del director desde el mapa
                    d_name = director_map.get(movie.get("director_id"), "Unknown Director").lower()
                    m_title = movie.get("title", "").lower()
                    score_title = fuzz.partial_ratio(search_query, m_title)
                    score_director = fuzz.partial_ratio(search_query, d_name)
                    # Lógica Case-Insensitive
                    if search_query not in m_title and search_query not in d_name and score_title < THRESHOLD and score_director < THRESHOLD:
                        continue

                    # Filtro de género
                    movie_genre = genre_map.get(movie.get("genre_id"), "Unknown")
                    if genre and genre.lower() not in movie_genre.lower():
                        continue
                    
                    clean_title = movie.get('title', '').lower().strip()
                    year = movie.get('year', '')
                    identifier = f"{clean_title}_{year}" 
                    movie["search_score"] = max(score_title, score_director)
                    identifier = f"{m_title}_{movie.get('year', '')}".strip()
                    
                    if identifier not in results_dict:
                        movie["content_type"] = "movie"
                        movie["genre_name"] = movie_genre
                        movie["director"] = director_map.get(movie.get("director_id"), "Unknown Director")
                        movie["platforms"] = [platform_name]
                        movie["unique_id"] = identifier  
                        movie["unique_id"] = identifier 
                        
                        results_dict[identifier] = movie
                    else:
                        if platform_name not in results_dict[identifier]["platforms"]:
                            results_dict[identifier]["platforms"].append(platform_name)
        except Exception as e:
            print(f"Error en búsqueda de películas: {e}")

        # --- Búsqueda en Series ---
        try:
            res = requests.get(f"{url}/series", headers={"X-API-KEY": key}, timeout=5)
            if res.status_code == 200:
                for serie in res.json():
                    s_title = serie.get("title", "").lower()
                    
                    # Resolver nombre del director para series
                    dir_data = serie.get("director")
                    if isinstance(dir_data, dict):
                        s_dir_name = dir_data.get("name", "Unknown Director").lower()
                    else:
                        s_dir_name = director_map.get(serie.get("director_id"), "Unknown Director").lower()

                    if search_query not in s_title and search_query not in s_dir_name:
                        continue

                    serie_genre = genre_map.get(serie.get("genre_id"), "Unknown")
                    if genre and genre.lower() not in serie_genre.lower():
                        continue
                    
                    identifier = f"{s_title}_{serie.get('start_year', '')}".strip()
                    
                    if identifier not in results_dict:
                        serie["content_type"] = "series"
                        serie["genre_name"] = serie_genre
                        serie["director"] = s_dir_name.title() # Aseguramos que tenga el campo director
                        serie["platforms"] = [platform_name]
                        serie["unique_id"] = identifier
                        results_dict[identifier] = serie
                    else:
                        if platform_name not in results_dict[identifier]["platforms"]:
                            results_dict[identifier]["platforms"].append(platform_name)
        except Exception as e:
            print(f"Error en búsqueda de series: {e}")

    # Convertir a lista
    final_results = list(results_dict.values())

    # 2. ORDENACIÓN PRIORITARIA: "Empieza por" primero, luego "Contiene"
    # True se ordena después de False, por eso usamos 'not' para que los que SI empiezan sean 0 (primero)
    final_results.sort(key=lambda x: (
        not x.get('title', '').lower().startswith(search_query),
        x.get('search_score', 0),  # Per relevancia de busqueda
        x.get('title', '').lower()
    ))

    return final_results
