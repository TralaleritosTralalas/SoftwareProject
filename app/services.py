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
    #all_movies = []
    movies_dict = {}

    for url, key, platform_name in PLATFORMS:
        
        # mapa de generos x plataforma
        genre_map = {}

        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        movies = get_local_movies(url, key)
        for movie in movies:
            #genre_id = movie.get("genre_id") #tenemos el id que se asocia con su correspondente genero en string
            #movie["genre_name"] = genre_map.get(genre_id, "Unknown")
            #movie["platform_name"] = platform_name
    
        #all_movies.extend(movies)
            identifier = f"{movie.get('title')}_{movie.get('year')}".lower().strip()
            
            if identifier not in movies_dict:
                movie["genre_name"] = genre_map.get(movie.get('genre_id'), "Unknown")
                movie["platforms"] = [platform_name]
                movie.pop("platform_name", None)
                movies_dict[identifier] = movie
            else:
                if platform_name not in movies_dict[identifier]["platforms"]:
                    movies_dict[identifier]["platforms"].append(platform_name)
    return list(movies_dict.values())

    
    #return all_movies

def get_all_series():  # obtener todas las peliculas de todas las "plataformas"
    all_series = []
    for url, key, platform_name in PLATFORMS:
        
        # mapa de generos x plataforma
        genre_map = {}

        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        series = get_local_series(url, key)
        for serie in series:
            genre_id = serie.get("genre_id") #tenemos el id que se asocia con su correspondente genero en string
            serie["genre_name"] = genre_map.get(genre_id, "Unknown")
            serie["platform_name"] = platform_name
    
        all_series.extend(series)
    
    return all_series




