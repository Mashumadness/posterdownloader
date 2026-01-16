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

| Categoría | Requisito | Color |
|---------|-----------|-------|
| **Excelente** | ≥ 3000 px | Verde |
| **Aceptable** | 2500–2999 px | Amarillo |
| **No recomendado** | < 2500 px | Rojo |

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

```text
PosterDownloader/
│
├── backend/
│   ├── app.py
│   ├── tmdb_service.py
│   ├── requirements.txt
│   └── .env              # NO subir al repositorio
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── styles.css
│
└── README.md

## 🌐 Ejecutar Frontend

### Opción recomendada (servidor local)

Desde la raíz del proyecto:

```bash
cd frontend
python -m http.server 8000
Luego abrir en el navegador:

http://127.0.0.1:8000

## 🌐 Ejecutar Backend

Desde la raíz del proyecto:

```bash
cd backend
python app.py
 