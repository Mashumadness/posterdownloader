import requests

API_KEY = "b8a9baed720480a8f2459ba242ac3dc3"

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/original"


def search_movie(query):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": query,
        "language": "en-US",
        "region": "US",
        "include_adult": False
    }

    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json().get("results", [])


def get_movie_images(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "append_to_response": "images",
        "language": "en-US"
    }

    r = requests.get(url, params=params)
    r.raise_for_status()

    posters = r.json().get("images", {}).get("posters", [])

    for p in posters:
        p["full_url"] = f"{IMAGE_BASE}{p['file_path']}"

    return posters
