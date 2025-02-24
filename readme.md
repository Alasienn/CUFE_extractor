# Proyecto: Validador de CSV en Django & Extractor de CUFE en Python

1. **Una app en Django** que revisa si los archivos CSV cumplen con ciertas reglas.
2. **Un script en Python** que busca el CUFE en archivos PDF y lo guarda en SQLite.

## 1.
### Se requiere
- Python 3.x
- Django 4.x
- pip

### Pasos
1. Clonar el repo
2. Crea y activar el entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```
   Para el caso de Windows se usa: venv\Scripts\activate

3. Instalarr las dependencias:
   ```bash
   pip install django
   ```
4. Configurr la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Ejecutar
   ```bash
   python manage.py runserver
   ```
6. Subiir un archivo CSV y revisar los resultados de la validación.

---

## 2. Extraer--CUFE
### Se requeire
- Python 3.x
- `pymupdf` (PyMuPDF)
- `sqlite3`

### Pasos
1. Clonarr el repo y entra a la carpeta del proyecto.
2. Instalar todo l necesario:
   ```bash
   pip install pymupdf
   ```
3. Ejecuta el script:
   ```bash
   python extract_cufe.py
   ```
4. Se pedira una ruta de un PDF.
5. Extrae el CUFE usando esta expresión regular: `\b([0-9a-fA-F]\n*){95,100}\b` y guarda  en SQLite:
   - Nombre del archivo
   - Número de páginas
   - CUFE encontrado
   - Peso del archivo

### BD
El script crea una base de datos `cufe_data.db` con una tabla `documentos` donde almacena la info extraída.

---

