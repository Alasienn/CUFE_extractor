import os
import re
import sqlite3
import fitz 



def extract_cufe_from_pdf(pdf_path):
    cufe_pattern = re.compile(r'\b([0-9a-fA-F]\n*){95,100}\b')
    
    with fitz.open(pdf_path) as doc:
        text = "\n".join(page.get_text("text") for page in doc)
        match = cufe_pattern.search(text)
        cufe = match.group() if match else None
        num_pages = len(doc)
    
    return cufe, num_pages

def save_to_db(pdf_path, cufe, num_pages):
    """ Guarda en SQLite."""
    db_path = "cufe_data.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_archivo TEXT,
            num_paginas INTEGER,
            cufe TEXT,
            peso INTEGER
        )
    ''')
    
	
    peso = os.path.getsize(pdf_path)
    nombre_archivo = os.path.basename(pdf_path)
    
    cursor.execute('''
        INSERT INTO documentos (nombre_archivo, num_paginas, cufe, peso)
        VALUES (?, ?, ?, ?)
    ''', (nombre_archivo, num_pages, cufe, peso))
    
    conn.commit()
    conn.close()

def main():
    pdf_path = input("Ingrese la ruta del archivo PDF: ").strip()
    
    if not os.path.exists(pdf_path):
        print("El archivo PDF no existe.")
        return
    
    cufe, num_pages = extract_cufe_from_pdf(pdf_path)
    
    
    
    if not cufe:
        print("No se encontró un CUFE válido en el documento.")
    else:
        save_to_db(pdf_path, cufe, num_pages)
        print("Dats guardados en la base de datos con éxito.")

if __name__ == "__main__":
    main()
