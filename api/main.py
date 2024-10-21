from fastapi import FastAPI, HTTPException
from datetime import datetime
import db_alumnat
import alumnat
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)

class alumne(BaseModel):
    IdAlumne: int
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: int
    Grup: str
    CreatedAt: datetime
    UpdatedAt: datetime

@app.get("/")
def read_root():
    return {"Alumnat"}

@app.get("/alumnes/list", response_model=List[dict])
def read_alumnes():
    return alumnat.alumnes_schema(db_alumnat.read())

@app.get("/alumnes/{id}", response_model=dict)
def read_alumnes_id(id: int):
    alumne_db = db_alumnat.read_id(id)
    if alumne_db is not None:
        return alumnat.alumne_schema(alumne_db)
    else:
        raise HTTPException(status_code=404, detail="Alumne no trobat")

@app.post("/alumne/add")
def add_alumne(new_alumne: alumne):
    aula = alumnat.read_aula_by_id(new_alumne.IdAula)
    if aula is None:
        raise HTTPException(status_code=404, detail="IdAula no existeix")
    result = db_alumnat.add_alumne(new_alumne)
    if result.get("status") == -1:
        raise HTTPException(status_code=500, detail=result["message"])
    return {"message": "Alumne afegit correctament"}

@app.put("/alumne/update/{id}")
def update_alumne(id: int, updated_alumne: alumne):
    aula = alumnat.read_aula_by_id(updated_alumne.IdAula)
    if aula is None:
        raise HTTPException(status_code=404, detail="IdAula no existeix")
    result = db_alumnat.update_alumne(id, updated_alumne)
    if result.get("status") == -1:
        raise HTTPException(status_code=500, detail=result["message"])
    return {"message": "S’ha modificat correctament"}

@app.delete("/alumne/delete/{id}")
def delete_alumne(id: int):
    result = db_alumnat.delete_alumne(id)
    if result.get("status") == -1:
        raise HTTPException(status_code=404, detail=result["message"])
    return {"message": "S’ha esborrat correctament"}

@app.get("/alumne/listAll", response_model=List[dict])
def list_all_alumnes():
    alumnes = db_alumnat.list_all_alumnes()
    return alumnat.alumnes_with_aula_schema(alumnes)
