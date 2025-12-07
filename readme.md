# 🎬 Poster Downloader (TMDB)
Aplicación simple para buscar películas usando **The Movie Database (TMDB)** y descargar pósters e imágenes promocionales en alta resolución.

Este proyecto está dividido en dos partes:

- **Backend (Flask – Python)** → Se comunica con la API de TMDB  
- **Frontend (HTML + CSS + JavaScript)** → Interfaz web que permite buscar películas y descargar imágenes

---

## 🚀 Funcionalidades actuales

✔️ Autocompletado en tiempo real mientras escribís  
✔️ Búsqueda de películas por título  
✔️ Lista de sugerencias ordenadas con año  
✔️ Visualización de los pósters disponibles  
✔️ Cada póster muestra su resolución  
✔️ Descargar cualquier imagen con un clic (abre el archivo en otra pestaña)  
✔️ Backend seguro (API Key guardada en archivo `.env`)  
✔️ Frontend y backend corriendo de forma local

---

## 📁 Estructura del proyecto

PosterDownloader/
│
├── backend/
│ ├── app.py
│ ├── tmdb_service.py
│ ├── requirements.txt
│ └── .env (NO se sube al repositorio)
│
└── frontend/
├── index.html
├── script.js
└── styles.css

yaml
Copiar código

---

## 🔧 Instalación del backend

### 1. Ir a la carpeta del backend

cd backend

shell
Copiar código

### 2. Instalar dependencias

pip install -r requirements.txt

go
Copiar código

### 3. Crear archivo `.env`

Dentro de `backend/` crear un archivo:

TMDB_API_KEY=tu_api_key_v3_aqui

yaml
Copiar código

⚠️ Importante: debe ser tu **API Key (v3 auth)** de TMDB.  
No es el token v4.

### 4. Ejecutar el backend

python app.py

yaml
Copiar código

El servidor se levantará en:

http://127.0.0.1:5000

yaml
Copiar código

---

## 🖥️ Levantar el frontend

Abrir otra terminal y ejecutar:

cd frontend
python -m http.server 8080

yaml
Copiar código

Frontend disponible en:

http://127.0.0.1:8080/index.html

yaml
Copiar código

---

## 🧪 Uso de la aplicación

1. Abrí el navegador en:  
   👉 `http://127.0.0.1:8080/index.html`

2. Escribí el nombre de una película (“cars”, “matrix”, etc).  
   → El autocompletado mostrará sugerencias.

3. Seleccioná una película.  
   → Debajo se mostrarán todos los pósters disponibles.

4. Hacé clic en cualquier imagen.  
   → Se abrirá en otra pestaña para que puedas guardarla en alta calidad.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Flask**
- **Requests**
- **dotenv**
- **HTML + CSS + JavaScript**
- **TMDB API**

---

## 🔐 Importante sobre la API Key

El archivo `.env` **no debe subirse al repositorio**.  
Asegurate de que `.gitignore` incluya:

backend/.env

yaml
Copiar código

---

## 🚧 Próximas mejoras (ideas)

- Filtros por resolución (ej: solo 4K)
- Descarga en ZIP de todas las imágenes
- Historial de búsquedas
- Tema oscuro
- Convertir en aplicación ejecutable (.exe)
- Servir frontend desde Flask (un solo servidor)

---

## 📝 Licencia

Proyecto para uso personal. TMDB requiere atribución si se utilizan imágenes públicamente.

---