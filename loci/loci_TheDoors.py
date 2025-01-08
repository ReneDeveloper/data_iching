#loci_TheDoors.py
import json
import os

# Datos a guardar en el archivo JSON para The Doors
the_doors_data = {
"People are strange": 38,#CONFIRMADO 20240917
    "The End": 63,#CONFIRMADO 20240917
    "Light My Fire": 30,
    "Riders on the Storm": 3,
    "Break On Through (To the Other Side)": 43

}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_the_doors.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(the_doors_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
