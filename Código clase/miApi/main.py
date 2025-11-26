from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# --- Modelo de Datos ---
# Usamos Pydantic para definir la estructura de nuestros datos.
# FastAPI lo usará para validación, serialización y documentación.

class Item(BaseModel):
    id: Optional[int] = None  # El ID será opcional al crear, pero presente al mostrar
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# --- Base de Datos "en memoria" ---
# Una lista simple que actuará como nuestra base de datos hardcodeada.
items_db = [
    Item(id=1, name="Platano", description="Una fruta amarilla y alargada", price=0.50, tax=0.05),
    Item(id=2, name="Manzana", description="Una fruta redonda, puede ser verde o roja", price=0.30, tax=0.04),
    Item(id=3, name="Pan", description="Pan de barra recien horneado", price=1.20, tax=0.10)
]

# --- Inicialización de la Aplicación ---
# Creamos la instancia de FastAPI.
app = FastAPI(
    title="API de Ejemplo para Clase",
    description="Una API sencilla con datos harcodeados para aprender los fundamentos de FastAPI y las operaciones CRUD.",
    version="1.0.0",
)


# --- Endpoints de la API (Operaciones CRUD) ---

# --- GET (Leer todos los items) ---
@app.get("/items", response_model=List[Item], tags=["Items"])
def get_all_items():
    """
    Recupera una lista de todos los items disponibles en la base de datos.
    """
    return items_db

# --- GET (Leer un item por su ID) ---
@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item_by_id(item_id: int):
    """
    Recupera un único item por su ID.
    Si el item no se encuentra, devuelve un error 404.
    """
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item no encontrado")

# --- POST (Crear un nuevo item) ---
@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(new_item: Item):
    """
    Crea un nuevo item y lo añade a la base de datos.
    El ID se genera automáticamente.
    """
    # Generamos un nuevo ID (simple, para este ejemplo)
    new_id = max(item.id for item in items_db) + 1 if items_db else 1
    new_item.id = new_id
    
    items_db.append(new_item)
    return new_item

# --- PUT (Actualizar un item existente) ---
@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
def update_item(item_id: int, updated_item: Item):
    """
    Actualiza un item existente identificado por su ID.
    Reemplaza completamente el item antiguo con el nuevo.
    Si el item no se encuentra, devuelve un error 404.
    """
    for index, item in enumerate(items_db):
        if item.id == item_id:
            # Asignamos el ID al item actualizado y lo reemplazamos en la lista
            updated_item.id = item_id
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item no encontrado")

# --- DELETE (Eliminar un item) ---
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: int):
    """
    Elimina un item de la base de datos por su ID.
    Si el item no se encuentra, devuelve un error 404.
    """
    item_found = False
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            item_found = True
            break
            
    if not item_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item no encontrado")
    
    # El código 204 No Content no debe devolver un cuerpo en la respuesta
    return 

# --- Endpoint Raíz ---
@app.get("/", include_in_schema=False)
def root():
    """
    Endpoint raíz que redirige a la documentación interactiva.
    """
    return {
        "message": "Bienvenido a la API de ejemplo. Visita /docs para ver la documentación interactiva (Swagger).",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

# Para ejecutar la app, guarda este archivo como main.py y ejecuta en la terminal:
# uvicorn main:app --reload
