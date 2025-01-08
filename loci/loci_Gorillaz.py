#loci_Gorillaz.py


import json
import os

# Datos a guardar en el archivo JSON para Gorillaz (ejemplos ficticios)
gorillaz_data = {
    "Feel Good Inc.": 47,
    "Clint Eastwood": 3,
    "DARE": 57,
    "On Melancholy Hill": 58,
    "Humility": 15,
    "Dirty Harry": 13,
    "Stylo": 31,
    "El Mañana": 24

#    "Feel Good Inc.": 42,
#    "Clint Eastwood": 3,
#    "DARE": 57,
#    "On Melancholy Hill": 47


}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_gorillaz.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(gorillaz_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
