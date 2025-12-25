from flask import Flask, request, jsonify
from flask_cors import CORS
from tmdb_service import search_movie, get_movie_images

app = Flask(__name__)
CORS(app)

@app.get("/api/search")
def api_search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify([])

    results = search_movie(q)

    return jsonify([
        {
            "id": r["id"],
            "title": r.get("title", ""),
            "year": (r.get("release_date") or "")[:4]
        }
        for r in results
    ])


@app.get("/api/images")
def api_images():
    movie_id = request.args.get("id")
    if not movie_id:
        return jsonify([])

    images = get_movie_images(movie_id)

    return jsonify([
        {
            "width": img["width"],
            "height": img["height"],
            "url": img["full_url"]
        }
        for img in images
    ])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
