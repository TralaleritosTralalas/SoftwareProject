import requests
from decouple import config

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


def get_all_movies():  # obtener todas las peliculas de todas las "plataformas"

    movies_dict = {} #diccionario para saber el contenido

    for url, key, platform_name in PLATFORMS:
        
        # mapa de generos x plataforma
        genre_map = {}

        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        movies = get_local_movies(url, key)
        for movie in movies:
            identifier = f"{movie.get('title')}_{movie.get('year')}".lower().strip() #identificador del contenido
            
            if identifier not in movies_dict: #el contenido no esta 
                movie["genre_name"] = genre_map.get(movie.get('genre_id'), "Unknown") #agarramos su genero
                movie["platforms"] = [platform_name]# lista de plataformas 
                movie.pop("platform_name", None) 
                movies_dict[identifier] = movie #guardamos en el diccionario
            else:
                if platform_name not in movies_dict[identifier]["platforms"]:
                    movies_dict[identifier]["platforms"].append(platform_name)
    return list(movies_dict.values())


def get_all_series():  # obtener todas las peliculas de todas las "plataformas"
    series_dict = {}

    for url, key, platform_name in PLATFORMS:
        genre_map = {}
        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        series = get_local_series(url, key)

        for serie in series:
            identifier = f"{serie.get('title')}_{serie.get('start_year', '')}".lower().strip()

            if identifier not in series_dict:
                serie["genre_name"] = genre_map.get(serie.get("genre_id"), "Unknown")
                serie["platforms"] = [platform_name]
                serie.pop("platform_name", None)
                series_dict[identifier] = serie
            else:
                if platform_name not in series_dict[identifier]["platforms"]:
                    series_dict[identifier]["platforms"].append(platform_name)
    
    return list(series_dict.values())


def search_content(query): #buscar peli o serie segun titulo
    results_dict = {}

    for url, key, platform_name in PLATFORMS:

        genre_map = {}
        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        # Buscar en movies
        try:
            response = requests.get(
                f"{url}/movies",
                headers={"X-API-KEY": key},
                params={"title": query},  # la API ya filtra por title con LIKE
                timeout=5
            )
            response.raise_for_status()
            for movie in response.json():
                movie["content_type"] = "movie"
                movie.setdefault("start_year", None)
                identifier = f"movie_{movie.get('title', '').lower().strip()}_{movie.get('year', '')}"
                if identifier not in results_dict:
                    movie["platforms"] = [platform_name]
                    movie["genre_name"] = genre_map.get(movie.get("genre_id"), "Unknown")
                    results_dict[identifier] = movie
                else:
                    if platform_name not in results_dict[identifier]["platforms"]:
                        results_dict[identifier]["platforms"].append(platform_name)
        except requests.exceptions.RequestException:
            pass  # plataforma no disponible, se ignora

        # Buscar en series
        try:
            response = requests.get(
                f"{url}/series",
                headers={"X-API-KEY": key},
                params={"title": query},
                timeout=5
            )
            response.raise_for_status()
            for serie in response.json():
                serie["content_type"] = "series"
                identifier = f"series_{serie.get('title', '').lower().strip()}_{serie.get('start_year', '')}"
                if identifier not in results_dict:
                    serie["platforms"] = [platform_name]
                    serie["genre_name"] = genre_map.get(serie.get("genre_id"), "Unknown")
                    results_dict[identifier] = serie
                else:
                    if platform_name not in results_dict[identifier]["platforms"]:
                        results_dict[identifier]["platforms"].append(platform_name)
        except requests.exceptions.RequestException:
            pass

    return list(results_dict.values())