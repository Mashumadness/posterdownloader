import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"


def search_movie(query):
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": API_KEY, "query": query}
    response = requests.get(url, params=params)
    return response.json().get("results", [])


def get_movie_images(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "append_to_response": "images"
    }
    data = requests.get(url, params=params).json()

    posters = data.get("images", {}).get("posters", [])

    # Construimos URLs completas para uso directo
    for poster in posters:
        poster["full_url"] = f"https://image.tmdb.org/t/p/original{poster['file_path']}"

    return posters
