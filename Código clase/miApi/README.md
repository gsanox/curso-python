# Mi API de Ejemplo con FastAPI

Esta es una API muy sencilla creada con Python y FastAPI. Su propósito es servir como ejemplo práctico para una clase, mostrando cómo implementar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) con datos harcodeados y cómo obtener documentación interactiva de forma automática.

## Características

- **Framework**: FastAPI
- **Servidor**: Uvicorn
- **Operaciones**: GET, POST, PUT, DELETE
- **Base de Datos**: Ninguna (los datos están en una lista en memoria)
- **Documentación**: Generada automáticamente con Swagger UI y ReDoc.

---

## Cómo Empezar

Sigue estos pasos para poner en funcionamiento la API en tu máquina local.

### 1. Prerrequisitos

- Tener Python 3.8 o superior instalado.

### 2. Instalación

1.  **Clona o descarga este repositorio.**

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    ```
    Y actívalo:
    - En Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3.  **Instala las dependencias:**
    Asegúrate de estar en el directorio donde se encuentra el archivo `requirements.txt` y ejecuta:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Ejecutar la API

Una vez instaladas las dependencias, ejecuta el siguiente comando en tu terminal:

```bash
uvicorn main:app --reload
```

- `main`: Es el nombre del archivo (`main.py`).
- `app`: Es el objeto `FastAPI` que creamos dentro del archivo (`app = FastAPI()`).
- `--reload`: Hace que el servidor se reinicie automáticamente cada vez que detecta un cambio en el código.

Verás una salida similar a esta, indicando que el servidor está funcionando:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx]
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

## Cómo Usar la API

La API estará disponible en `http://127.0.0.1:8000`.

### Documentación Interactiva (Swagger)

La mejor forma de explorar y probar la API es a través de la documentación de Swagger. Para acceder a ella, abre tu navegador y ve a:

**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

Desde esta interfaz podrás:
- Ver todos los endpoints disponibles.
- Conocer los modelos de datos (schemas) para las peticiones y respuestas.
- **Ejecutar peticiones de prueba** directamente desde el navegador y ver los resultados en tiempo real.

### Documentación Alternativa (ReDoc)

FastAPI también genera otra vista de la documentación con ReDoc. Puedes verla en:

**[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)**

# Referencias
- https://kinsta.com/es/blog/fastapi/
