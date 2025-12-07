import requests
import urllib.parse

API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOGE5YmFlZDcyMDQ4MGE4ZjI0NTliYTI0MmFjM2RjMyIsIm5iZiI6MTc2NTEyODY4MS4zNzQsInN1YiI6IjY5MzViOWU5NjhlYTMwZWJiYTI0M2UxYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.sgdhRohaED7XF7wPlFJHctSLqjuV2UImhXYli5CkpuI77"

def buscar_pelicula(nombre):
    nombre_codificado = urllib.parse.quote(nombre)
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={nombre_codificado}"
    r = requests.get(url).json()

    if not r["results"]:
        print("No se encontró ninguna película con ese nombre.")
        return None

    return r["results"][0]  # primer resultado


def obtener_poster_original(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&append_to_response=images"
    data = requests.get(url).json()

    posters = data.get("images", {}).get("posters", [])
    if not posters:
        print("La película no tiene pósters disponibles.")
        return None

    # selecciona el de mayor resolución (normalmente el primero)
    poster_path = posters[0]["file_path"]

    # URL final en máxima resolución (original)
    final_url = f"https://image.tmdb.org/t/p/original{poster_path}"

    return final_url


def main():
    nombre = input("Ingresá el nombre de la película: ")

    pelicula = buscar_pelicula(nombre)
    if not pelicula:
        return

    print(f"\nPelícula encontrada: {pelicula['title']} ({pelicula.get('release_date', '')[:4]})")

    poster_url = obtener_poster_original(pelicula["id"])

    if poster_url:
        print("\n📥 URL del póster en máxima resolución:")
        print(poster_url)
        print("\nCopiala en el navegador para descargar la imagen.")


if __name__ == "__main__":
    main()
