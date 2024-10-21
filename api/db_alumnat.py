from client import db_client
from datetime import datetime

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Alumne")
        alumnes = cur.fetchall()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}"}
    finally:
        conn.close()
    
    return alumnes

def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Alumne WHERE IdAlumne = %s", (id,))
        alumne = cur.fetchone()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        conn.close()

    return alumne

def add_alumne(new_alumne):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Alumne (IdAlumne, IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (new_alumne.IdAlumne, new_alumne.IdAula, new_alumne.NomAlumne, new_alumne.Cicle, new_alumne.Curs,
              new_alumne.Grup, new_alumne.CreatedAt, new_alumne.UpdatedAt))
        conn.commit()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        conn.close()
    
    return {"status": 0, "message": "Alumne afegit correctament"}

def update_alumne(id, updated_alumne):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("""
            UPDATE Alumne 
            SET IdAula = %s, NomAlumne = %s, Cicle = %s, Curs = %s, Grup = %s, UpdatedAt = %s 
            WHERE IdAlumne = %s
        """, (updated_alumne.IdAula, updated_alumne.NomAlumne, updated_alumne.Cicle,
              updated_alumne.Curs, updated_alumne.Grup, datetime.now(), id))
        conn.commit()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        conn.close()
    
    return {"status": 0, "message": "S’ha modificat correctament"}

def delete_alumne(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("DELETE FROM Alumne WHERE IdAlumne = %s", (id,))
        conn.commit()
        if cur.rowcount == 0:
            return {"status": -1, "message": "No s'ha trobat l'alumne"}
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        conn.close()
    
    return {"status": 0, "message": "S’ha esborrat correctament"}

def list_all_alumnes():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("""
            SELECT a.*, au.DescAula, au.Edifici, au.Pis 
            FROM Alumne a
            JOIN Aula au ON a.IdAula = au.IdAula
        """)
        alumnes = cur.fetchall()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        conn.close()
    
    return alumnes
