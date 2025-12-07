const searchInput = document.getElementById("search");
const suggestions = document.getElementById("suggestions");
const postersDiv = document.getElementById("posters");
const titleHeader = document.getElementById("selected-title");
const qualityFilter = document.getElementById("quality-filter");
const sortBtn = document.getElementById("sort-btn");

let debounceTimer = null;
let currentImages = [];
let sortDirection = "desc"; // desc = mayor → menor, asc = menor → mayor

// ------------------------------------
// Evento input (autocompletar)
// ------------------------------------
searchInput.addEventListener("input", () => {
    const q = searchInput.value.trim();

    if (debounceTimer) clearTimeout(debounceTimer);

    if (q.length < 2) {
        suggestions.innerHTML = "";
        return;
    }

    debounceTimer = setTimeout(() => {
        fetch(`http://127.0.0.1:5000/api/search?q=${q}`)
            .then(res => res.json())
            .then(data => {
                suggestions.innerHTML = "";
                data.forEach(movie => {
                    const div = document.createElement("div");
                    div.className = "suggestion";
                    div.innerText = `${movie.title} (${movie.year})`;
                    div.onclick = () => selectMovie(movie);
                    suggestions.appendChild(div);
                });
            });
    }, 250);
});


// ------------------------------------
// Seleccionar película
// ------------------------------------
function selectMovie(movie) {
    titleHeader.innerText = `${movie.title} (${movie.year})`;
    suggestions.innerHTML = "";
    searchInput.value = movie.title;

    fetch(`http://127.0.0.1:5000/api/images?id=${movie.id}`)
        .then(res => res.json())
        .then(list => {
            currentImages = list;
            renderImages();
        });
}


// ------------------------------------
// Renderizar posters con filtro + orden
// ------------------------------------
function renderImages() {
    postersDiv.innerHTML = "";

    let filtered = currentImages.filter(img => {
        const res = Math.max(img.width, img.height);

        if (qualityFilter.value === "excellent") return res >= 3000;
        if (qualityFilter.value === "acceptable") return res >= 2500 && res < 3000;
        if (qualityFilter.value === "poor") return res < 2500;

        return true;
    });

    // Ordenar por resolución
    filtered.sort((a, b) => {
        const A = Math.max(a.width, a.height);
        const B = Math.max(b.width, b.height);

        return sortDirection === "desc" ? B - A : A - B;
    });

    filtered.forEach(img => {
        const maxRes = Math.max(img.width, img.height);
        let tagClass = "poor";
        let tagText = "No recomendado";

        if (maxRes >= 3000) {
            tagClass = "excellent";
            tagText = "Excelente";
        } else if (maxRes >= 2500) {
            tagClass = "acceptable";
            tagText = "Aceptable";
        }

        const card = document.createElement("div");
        card.className = "poster-card";
        card.innerHTML = `
            <img src="${img.url}" class="poster-img" />
            <div class="tag res">${img.width} × ${img.height}</div>
            <div class="tag ${tagClass}">${tagText}</div>
        `;
        card.onclick = () => window.open(img.url, "_blank");

        postersDiv.appendChild(card);
    });
}


// ------------------------------------
// Evento filtro
// ------------------------------------
qualityFilter.addEventListener("change", renderImages);


// ------------------------------------
// Evento ordenar
// ------------------------------------
sortBtn.addEventListener("click", () => {
    sortDirection = sortDirection === "desc" ? "asc" : "desc";

    sortBtn.innerText = sortDirection === "desc"
        ? "Ordenar por resolución (Mayor → menor)"
        : "Ordenar por resolución (Menor → mayor)";

    renderImages();
});
