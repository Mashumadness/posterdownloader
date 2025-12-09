import subprocess
import time
import webview
import threading
import requests

# Ruta correcta al Python REAL
PYTHON = r"C:\Users\msuar\AppData\Local\Programs\Python\Python313\python.exe"

BACKEND_PATH = r"C:\Users\msuar\Desktop\PosterDownloader\app\backend\app.py"
BACKEND_URL = "http://127.0.0.1:5000"


def start_backend():
    print("[Launcher] Iniciando Flask en:", BACKEND_PATH)
    subprocess.Popen([PYTHON, BACKEND_PATH])
    print("[Launcher] Flask iniciado correctamente")


def wait_for_backend():
    print("[Launcher] Esperando a Flask...")
    while True:
        try:
            requests.get(BACKEND_URL)
            print("[Launcher] Flask está activo")
            break
        except Exception:
            time.sleep(0.5)


def open_window():
    print("[Launcher] Iniciando ventana...")
    webview.create_window("Poster Downloader", BACKEND_URL)
    webview.start()


if __name__ == '__main__':
    print("[Launcher] Ejecutando launcher...")

    threading.Thread(target=start_backend, daemon=True).start()
    wait_for_backend()
    open_window()
