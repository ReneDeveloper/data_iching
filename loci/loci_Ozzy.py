#loci_Ozzy.py
import json
import os

# Datos a guardar en el archivo JSON para Ozzy Osbourne
ozzy_data = {
"War Pigs": 7,#CONFIRMADO 20240917
    "Paranoid": 39,
    "Crazy Train": 57,
    "Iron Man": 26,
    "Mr. Crowley": 43,
    
    "Bark at the Moon": 45,
    "Heaven and Hell": 50,
    "No More Tears": 31
}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_ozzy.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(ozzy_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
