import csv
import re
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Expresión
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Valores columna 3
VALID_VALUES_COL3 = {'CC', 'TI'}
# Rango columna 4
MIN_VALUE_COL4 = 500000
MAX_VALUE_COL4 = 1500000

def validate_csv(file):
    errors = []
    file_data = file.read().decode('utf-8').splitlines()
    reader = csv.reader(file_data)
    
    for i, row in enumerate(reader, start=1):
        if len(row) != 5:
            errors.append(f"Fila {i}: Número incorrecto de columnas")
            continue

        col1, col2, col3, col4, col5 = row
        
        
        # Validación col  1
        if not col1.isdigit() or not (3 <= len(col1) <= 10):
            errors.append(f"Fila {i}: Columna 1 inválida")
        
        # Validación col 2 
        if not re.match(EMAIL_REGEX, col2):
            errors.append(f"Fila {i}: Columna 2 inválida")
        
        # Validación col 3
        if col3 not in VALID_VALUES_COL3:
            errors.append(f"Fila {i}: Columna 3 inválida")
        
        # Validación col 4 
        try:
            col4_value = int(col4)
            if not (MIN_VALUE_COL4 <= col4_value <= MAX_VALUE_COL4):
                errors.append(f"Fila {i}: Columna 4 fuera de rango")
        except ValueError:
            errors.append(f"Fila {i}: Columna 4 no es un número válido")
    
    return errors

def upload_file(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        file = request.FILES['csv_file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        errors = validate_csv(file)
        
        if errors:
            return render(request, 'upload.html', {'errors': errors})
        
        return render(request, 'upload.html', {'success': "Archivo validado correctamente"})
    
    return render(request, 'upload.html')
