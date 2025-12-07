# 🎬 Poster Downloader (TMDB)
Aplicación simple y rápida para buscar películas y descargar pósters en alta calidad usando la API de **TheMovieDB (TMDB)**.

Diseñada para uso personal — ideal para quienes imprimen imágenes en gran formato (por ejemplo, **sublimación en aluminio A4**) y necesitan asegurarse de que los pósters tengan **resolución suficiente**.

---

## 🚀 Funcionalidades actuales

### 🔍 1. Búsqueda con autocompletado
- A medida que escribís el nombre de una película, se muestran sugerencias.
- Los datos provienen directamente de la API de TMDB.

### 🎞️ 2. Visualización de todos los pósters disponibles
- La app muestra todas las imágenes de TMDB para esa película.
- Cada póster incluye:
  - Miniatura
  - Resolución (ancho × alto)
  - Clasificación automática de calidad

### 🏷️ 3. Clasificación automática de calidad
Según la resolución máxima (ancho o alto):

| Categoría       | Requisito          | Color |
|----------------|--------------------|-------|
| **Excelente**  | ≥ 3000 px          | Verde |
| **Aceptable**  | 2500–2999 px       | Amarillo |
| **No recomendado** | < 2500 px     | Rojo |

Pensado específicamente para saber rápidamente qué imágenes sirven para sublimación A4.

### 🧩 4. Filtros por calidad
Podés mostrar únicamente:
- Todas
- Solo **Excelente**
- Solo **Aceptable**
- Solo **No recomendado**

### 📏 5. Ordenar por resolución
Un botón permite alternar:
- **Mayor → menor**
- **Menor → mayor**

Ideal para encontrar la imagen más grande primero.

---

## 🛠️ Estructura del proyecto

PosterDownloader/
│
├── backend/
│ ├── app.py
│ ├── tmdb_service.py
│ ├── requirements.txt
│ └── .env (NO subir al repositorio)
│
├── frontend/
│ ├── index.html
│ ├── script.js
│ └── styles.css
│
└── readme.md

yaml
Copiar código

---

## ⚙️ Instalación (Backend)

### 1. Crear entorno virtual (opcional, recomendado)

```sh
python -m venv venv
Activar:

Windows:

sh
Copiar código
venv\Scripts\activate
2. Instalar dependencias
sh
Copiar código
pip install -r requirements.txt
3. Crear archivo .env
Dentro de /backend/.env:

ini
Copiar código
TMDB_API_KEY=TU_API_KEY_AQUI
Asegurate de no subir .env al repo.

4. Ejecutar backend
Desde /backend/:

sh
Copiar código
python app.py
El servidor inicia en:

cpp
Copiar código
http://127.0.0.1:5000
🌐 Ejecutar frontend
Abrí este archivo en Chrome:

bash
Copiar código
frontend/index.html
O ejecutá un server local:

bash
Copiar código
cd frontend
python -m http.server 8080
Accedé en:

cpp
Copiar código
http://127.0.0.1:8080
🔌 Endpoints disponibles (Backend)
/api/search?q=<texto>
Devuelve lista de películas coincidentes.

/api/images?id=<movie_id>
Devuelve todas las imágenes (pósters) de TMDB para la película seleccionada, incluyendo:

json
Copiar código
{
  "url": "https://image.tmdb.org/t/p/original/abcd1234.jpg",
  "width": 3000,
  "height": 4500
}
🧠 Lógica de filtrado (Frontend)
Se clasifican imágenes según su resolución máxima.

Los filtros y el ordenamiento se aplican sin recargar la página.

El usuario puede:

Filtrar por calidad

Ordenar por resolución

Ver tarjetas con color de estado

🙌 Próximas mejoras sugeridas
Estas funciones ya están pensadas pero no implementadas todavía:

✔ Descargar todos los pósters en ZIP
✔ Modo oscuro
✔ Favoritos localmente (LocalStorage)
✔ Vista tipo “Pinterest” compacta
✔ Zoom al pasar el mouse
✔ Mostrar tamaño aproximado en centímetros a 300DPI
Si querés, las vamos haciendo una por una.

📜 Licencia
Uso personal. No está permitido redistribuir imágenes de TMDB.
Cumple con los términos de uso: https://www.themoviedb.org/documentation/api/terms-of-use
