"""
import requests

def get_local_movies():
    url = "http://127.0.0.1:8080'''" # Tu API local
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Lanza error si hay fallos (404, 500, etc.)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error conectando a la API: {e}")
        return []
        """