#loci_LinkinPark.py


import json
import os

# Datos actualizados a guardar en el archivo JSON para Linkin Park
linkin_park_data = {
    #"In the End": 32,
    #"Numb": 45,
    #"Crawling": 19,
    #"Faint": 7


    "In the End": 63,
    "Numb": 47,
    "Crawling": 29,
    "Faint": 32
}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_linkin_park.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(linkin_park_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
