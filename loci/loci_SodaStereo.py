#loci_SodaStereo.py
import json
import os

# Datos con las asociaciones entre temas de Soda Stereo y hexagramas del I Ching (ejemplo ficticio)
soda_stereo_data = {
    "De Música Ligera": 25,
    "Persiana Americana": 40,
    "En la Ciudad de la Furia": 36,#OK
    "Cuando Pase el Temblor": 21,
    "Signos": 14,#OK
    "Prófugos": 11,
    "Nada Personal": 48,
    "Zoom": 52
}

# Nombre del archivo JSON y ruta donde se guardará
nombre_archivo = 'loci_soda_stereo.json'
ruta_guardado = '../json/'

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Guardar los datos en el archivo JSON
ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
with open(ruta_completa, 'w', encoding='utf-8') as file:
    json.dump(soda_stereo_data, file, ensure_ascii=False, indent=4)

print(f"Archivo '{ruta_completa}' creado con éxito.")
