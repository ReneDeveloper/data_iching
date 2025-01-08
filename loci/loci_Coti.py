#loci_Coti.py

import json
import os

# Datos a guardar en el archivo JSON para Coti (ejemplos ficticios)
coti_data = {
    "Nada fue un error": 18,
    "Color Esperanza": 57,
    "Otra vez": 24,
    "Tu nombre": 1,
    "Antes que ver el sol": 35,
    "Te quise tanto": 16,
    "Cómo dueles en los labios": 30,
    "Perdóname": 31
}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_coti.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(coti_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
