#loci_IronMaiden.py


import json
import os

# Datos a guardar en el archivo JSON para Iron Maiden
iron_maiden_data = {
"The Clairvoyant": 20,#AGREGADO_MANUAL 20240917
    "2 Minutes to Midnight": 5,#AGREGADO_MANUAL 20240917
    "The Trooper": 7,
    "The Number of the Beast": 63,
    "Run to the Hills": 35,
    "Fear of the Dark": 47,
    
    "Hallowed Be Thy Name": 64,
    "Aces High": 41,
    "Iron Maiden": 54

}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_iron_maiden.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(iron_maiden_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
