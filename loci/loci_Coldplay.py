#loci_Coldplay.py

import json
import os

# Datos con las asociaciones entre temas de Coldplay y hexagramas del I Ching (ejemplos ficticios)
coldplay_data = {
    "Fix You": 4,
    "Viva la Vida": 16,
    "Yellow": 57,
    "The Scientist": 50,
    "Clocks": 32,
    "Paradise": 37,
    "Adventure of a Lifetime": 19,
    "Something Just Like This": 22
}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_coldplay.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(coldplay_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
