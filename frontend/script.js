const API_BASE = "http://127.0.0.1:5000";

const searchInput = document.getElementById("search");
const suggestions = document.getElementById("suggestions");
const postersDiv = document.getElementById("posters");
const titleHeader = document.getElementById("selected-title");
const qualityFilter = document.getElementById("quality-filter");
const sortBtn = document.getElementById("sort-btn");

let debounceTimer = null;
let currentImages = [];
let sortDirection = "desc";

// -------- SEARCH --------
searchInput.addEventListener("input", () => {
    const q = searchInput.value.trim();
    if (debounceTimer) clearTimeout(debounceTimer);

    if (q.length < 2) {
        suggestions.innerHTML = "";
        suggestions.style.display = "none";
        return;
    }

    debounceTimer = setTimeout(() => {
        fetch(`${API_BASE}/api/search?q=${encodeURIComponent(q)}`)
            .then(r => r.json())
            .then(data => {
                suggestions.innerHTML = "";
                if (data.length > 0) {
                    suggestions.style.display = "block";
                    data.forEach(m => {
                        const d = document.createElement("div");
                        d.className = "suggestion";
                        d.innerText = `${m.title} (${m.year})`;
                        d.onclick = () => selectMovie(m);
                        suggestions.appendChild(d);
                    });
                }
            })
            .catch(err => {
                console.error("Error buscando películas:", err);
            });
    }, 300);
});

// Close suggestions when clicking outside
document.addEventListener("click", (e) => {
    if (!searchInput.contains(e.target) && !suggestions.contains(e.target)) {
        suggestions.style.display = "none";
    }
});

// -------- SELECT MOVIE --------
function selectMovie(movie) {
    titleHeader.innerText = `${movie.title} (${movie.year})`;
    suggestions.innerHTML = "";
    suggestions.style.display = "none";
    searchInput.value = movie.title;

    fetch(`${API_BASE}/api/images?id=${movie.id}`)
        .then(r => r.json())
        .then(list => {
            currentImages = list;
            renderImages();
        })
        .catch(err => {
            console.error("Error cargando imágenes:", err);
        });
}

// -------- RENDER IMAGES --------
function renderImages() {
    postersDiv.innerHTML = "";

    let filtered = currentImages.filter(img => {
        const r = Math.max(img.width, img.height);
        if (qualityFilter.value === "excellent") return r >= 3000;
        if (qualityFilter.value === "acceptable") return r >= 2500 && r < 3000;
        if (qualityFilter.value === "poor") return r < 2500;
        return true;
    });

    filtered.sort((a, b) => {
        const A = Math.max(a.width, a.height);
        const B = Math.max(b.width, b.height);
        return sortDirection === "desc" ? B - A : A - B;
    });

    filtered.forEach(img => {
        const card = document.createElement("div");
        card.className = "poster-card";

        card.innerHTML = `
            <div class="poster-img-container">
                <img src="${img.url}" class="poster-img" alt="Poster">
                <div class="tag res">${img.width} × ${img.height}</div>
            </div>
            <div class="card-actions">
                <button class="download-btn">⬇ Descargar HD</button>
            </div>
        `;

        card.querySelector(".poster-img-container").onclick = () => {
            window.open(img.url, "_blank");
        };

        card.querySelector(".download-btn").onclick = (e) => {
            e.stopPropagation();
            window.location.href = `${API_BASE}/api/download?url=${encodeURIComponent(img.url)}`;
        };

        postersDiv.appendChild(card);
    });
}

// -------- EVENTS --------
qualityFilter.addEventListener("change", renderImages);

sortBtn.addEventListener("click", () => {
    sortDirection = sortDirection === "desc" ? "asc" : "desc";
    sortBtn.textContent = sortDirection === "desc" ? "↓ Mayor a menor" : "↑ Menor a mayor";
    renderImages();
});