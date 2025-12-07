from flask import Flask, request, jsonify
from flask_cors import CORS
from tmdb_service import search_movie, get_movie_images

app = Flask(__name__)
CORS(app)  # Permite llamadas desde frontend

@app.get("/api/search")
def api_search():
    query = request.args.get("q", "")
    if not query:
        return jsonify([])
    results = search_movie(query)
    simplified = [
        {
            "id": r["id"],
            "title": r["title"],
            "year": (r.get("release_date") or "")[:4]
        }
        for r in results
    ]
    return jsonify(simplified)


@app.get("/api/images")
def api_images():
    movie_id = request.args.get("id")
        # No recibimos id → devolvemos lista vacía
    if not movie_id:
        return jsonify([])

    images = get_movie_images(movie_id)
    simplified = [
        {
            "file_path": img["file_path"],
            "width": img["width"],
            "height": img["height"],
            "url": img["full_url"]
        }
        for img in images
    ]
    return jsonify(simplified)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
