from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from tmdb_service import search_movie, get_movie_images
import requests
import tempfile
import os

app = Flask(__name__)
CORS(app)

# ---------------- SEARCH ----------------
@app.get("/api/search")
def api_search():
    query = request.args.get("q", "")
    if not query:
        return jsonify([])

    results = search_movie(query)
    return jsonify([
        {
            "id": r["id"],
            "title": r["title"],
            "year": (r.get("release_date") or "")[:4]
        }
        for r in results
    ])

# ---------------- IMAGES ----------------
@app.get("/api/images")
def api_images():
    movie_id = request.args.get("id")
    if not movie_id:
        return jsonify([])

    images = get_movie_images(movie_id)

    return jsonify([
        {
            "url": img["full_url"],
            "width": img["width"],
            "height": img["height"]
        }
        for img in images
    ])

# ---------------- DOWNLOAD (KEY) ----------------
@app.get("/api/download")
def api_download():
    url = request.args.get("url")
    if not url:
        return "Missing url", 400

    r = requests.get(url, stream=True)
    if r.status_code != 200:
        return "Failed to download image", 500

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    for chunk in r.iter_content(8192):
        tmp.write(chunk)
    tmp.close()

    return send_file(
        tmp.name,
        as_attachment=True,
        download_name="poster.jpg"
    )

if __name__ == "__main__":
    app.run(port=5000, debug=True)
