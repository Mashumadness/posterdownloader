const searchInput = document.getElementById("search");
const suggestions = document.getElementById("suggestions");
const postersDiv = document.getElementById("posters");
const titleHeader = document.getElementById("selected-title");

let debounceTimer = null;

// Evento de escritura en el input
searchInput.addEventListener("input", () => {
    const q = searchInput.value.trim();

    if (debounceTimer) clearTimeout(debounceTimer);

    // No buscar si escribió menos de 2 caracteres
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
            })
            .catch(err => {
                console.error("ERROR FETCHING SEARCH:", err);
            });
    }, 250);
});

// Seleccionar película
function selectMovie(movie) {
    titleHeader.innerText = `${movie.title} (${movie.year})`;
    suggestions.innerHTML = "";
    searchInput.value = movie.title;

    fetch(`http://127.0.0.1:5000/api/images?id=${movie.id}`)
        .then(res => res.json())
        .then(list => {
            postersDiv.innerHTML = "";

            list.forEach(img => {
                const card = document.createElement("div");
                card.className = "poster-card";

                card.innerHTML = `
                    <img src="${img.url}" class="poster-img" />
                    <p>${img.width} × ${img.height}</p>
                `;

                card.onclick = () => window.open(img.url, "_blank");

                postersDiv.appendChild(card);
            });
        })
        .catch(err => {
            console.error("ERROR FETCHING IMAGES:", err);
        });
}
