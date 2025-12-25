import requests
import urllib.parse

API_KEY = "b8a9baed720480a8f2459ba242ac3dc3"

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/original"


def buscar_pelicula(nombre):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": nombre,
        "language": "en-US",
        "region": "US"
    }

    r = requests.get(url, params=params)
    r.raise_for_status()

    results = r.json().get("results", [])
    if not results:
        print("No se encontró la película")
        return None

    return results[0]


def obtener_poster(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "append_to_response": "images"
    }

    r = requests.get(url, params=params)
    r.raise_for_status()

    posters = r.json().get("images", {}).get("posters", [])
    if not posters:
        return None

    return f"{IMAGE_BASE}{posters[0]['file_path']}"


if __name__ == "__main__":
    nombre = input("Película: ").strip()
    peli = buscar_pelicula(nombre)
    if peli:
        print(peli["title"])
        print(obtener_poster(peli["id"]))
