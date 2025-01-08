loci_Amaral.py

import json
import os

# Datos con las asociaciones entre temas de Amaral y hexagramas del I Ching (corregido)
amaral_data = {
    "Moriría por Vos": 37,
    "El Universo Sobre Mí": 15,
    "Sin Ti No Soy Nada": 24,
    "Te Necesito": 4,
    "Kamikaze": 51,
    "Resurrección": 21,
    "Mi Alma Perdida": 29,
    "Salir Corriendo": 43

#    "Moriría por Vos": 27,
#    "El Universo Sobre Mí": 1,
#    "Sin Ti No Soy Nada": 42,
#    "Te Necesito": 58,
#    "Kamikaze": 31,
#    "Resurrección": 50,
#    "Mi Alma Perdida": 3,
#    "Salir Corriendo": 32


}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_amaral.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(amaral_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
