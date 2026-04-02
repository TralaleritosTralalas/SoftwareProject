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

def get_all_movies(): #obtener todas las peliculas de todas las "plataformas"
    movies = []
    for url, key in [
        (url_local_1, api_key_local_1),
        (url_local_2, api_key_local_2),
        (url_local_3, api_key_local_3),
    ]:
        movies.extend(get_local_movies(url, key))

        #gestionar los generos de las peliculas
        genres = get_genre(url, key) 
        for g in genres:
            genre_map[g["id"]] = g["name"]
        for movie in movies:
            gendre_id = movie.get("genre")
            movie["genre_name"] = genre_map.get(genre_id, "Unknown")

    return movies

def get_genre(url, api_key): #
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