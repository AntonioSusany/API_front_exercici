from client import db_client

def alumne_schema(alumne) -> dict:
    return {
        "IdAlumne": alumne[0],
        "IdAula": alumne[1],
        "NomAlumne": alumne[2],
        "Cicle": alumne[3],
        "Curs": alumne[4],
        "Grup": alumne[5],
        "CreatedAt": alumne[6],
        "UpdatedAt": alumne[7]
    }

def alumne_with_aula_schema(alumne) -> dict:
    return {
        "IdAlumne": alumne[0],
        "IdAula": alumne[1],
        "NomAlumne": alumne[2],
        "Cicle": alumne[3],
        "Curs": alumne[4],
        "Grup": alumne[5],
        "CreatedAt": alumne[6],
        "UpdatedAt": alumne[7],
        "Edifici": alumne[9],
        "Pis": alumne[10]
    }

def alumnes_schema(alumnes) -> list:
    return [alumne_schema(alumne) for alumne in alumnes]

def alumnes_with_aula_schema(alumnes) -> list:
    return [alumne_with_aula_schema(alumne) for alumne in alumnes]

def read_aula_by_id(id_aula):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Aula WHERE IdAula = %s", (id_aula,))
        aula = cur.fetchone()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        conn.close()
    
    return aula
