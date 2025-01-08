#loci_PinkFloyd.py

import json
import os

# Datos con las asociaciones entre temas de Pink Floyd y hexagramas del I Ching (ejemplos ficticios)
pink_floyd_data = {
"Money": 36,#CONFIRMADO


    "Comfortably Numb": 5,
    "Wish You Were Here": 63,
    "Another Brick in the Wall (Part II)": 23,
    "Time": 43,
    
    "Shine On You Crazy Diamond": 64,
    "Hey You": 44,
    "Brain Damage / Eclipse": 29
}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_pink_floyd.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(pink_floyd_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
