#sinonimos_49_64.py

import json
import os

# Sinónimos únicos de los hexagramas del 49 al 64 con al menos 8 sinónimos
sinonimos_hexagramas = {
    "49": ["Revolución", "Moldeamiento", "Reforma", "Transformación", "Cambio", "Renovación", "Innovación", "Metamorfosis"],
    "50": ["Olla", "Caldero", "Cazuela", "Recipiente", "Vaso", "Vasija", "Contenedor", "Vajilla"],
    "51": ["Trueno", "Trueno Atronador", "Trueno Retumbante", "Trueno que Retumba", "Trueno del Cielo", "Trueno de Arriba", "Trueno Celestial", "Sonido del Trueno"],
    "52": ["Montaña", "Colina", "Monte", "Cumbre", "Pico", "Cerro", "Elevación", "Altura"],
    "53": ["Progreso", "Avance", "Desarrollo", "Evolución", "Crecimiento", "Mejora", "Ascenso", "Adelanto"],
    "54": ["Joven que se Casa", "Doncella que se Casa", "Novia", "Mujer Joven que se Casa", "Dama que se Casa", "Joven Casada", "Doncella Casada", "Mujer Joven Casada"],
    "55": ["Abundancia", "Plenitud", "Plétora", "Profusión", "Riqueza", "Opulencia", "Fartura", "Gran Abundancia"],
    "56": ["Viajero", "Peregrino", "Caminante", "Andariego", "Nómada", "Errante", "Ambulante", "Trotamundos"],
    "57": ["Viento", "Viento Suave", "Viento Del Cielo", "Viento de Arriba", "Viento Celestial", "Penetración", "Penetración Suave", "Penetración del Viento"],
    "58": ["Alegría", "Expansión", "Felicidad", "Diversión", "Divertida", "Jovialidad", "Plenitud", "Abundancia"],
    "59": ["Disolución", "Dispensación", "Disipación", "Distribución", "Sepultura", "Dispersión", "Regeneración", "Propagación"],
    "60": ["Restricción", "Limitación", "Restraint", "Limitación del Agua", "Restricción del Agua", "Interior", "Verdadero Interior", "Realidad Interior"],
    "61": ["Interior Verdadero", "Verdadero Interior", "Realidad Interior", "Interior", "Verdadero Interior", "Realidad Interior", "Verdadero Interior", "Realidad Interior"],
    "62": ["Preponderancia del Pequeño", "Preponderancia de lo Pequeño", "Preponderancia de lo Blando", "Preponderancia de lo Moderado", "Preponderancia de lo Menor", "Preponderancia de lo Flexible", "Preponderancia de lo Manso", "Preponderancia de lo Adaptable"],
    "63": ["Conclusión","Realización","Finalización","Culminación","Perfección","Cumplimiento","Consumación","Cierre"],
    "64": ["No Completado", "No Completar", "No Llegar a Completar", "No Alcanzar a Completar", "No Lograr Completar", "No Alcanzar Completar", "No Lograr la Completitud", "No Alcanzar la Completitud"]
}






# Ruta base donde se guardarán los archivos JSON
ruta_base = '../json/'

# Función para guardar el archivo JSON
def guardar_json(data, nombre_archivo):
    ruta_archivo = os.path.join(ruta_base, nombre_archivo)
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Archivo '{ruta_archivo}' creado con éxito.")

# Guardar cada archivo JSON para los hexagramas del 49 al 64
for numero_hexagrama, sinonimos in sinonimos_hexagramas.items():
    nombre_archivo = f'sinonimos_{numero_hexagrama}.json'
    data = {numero_hexagrama: sinonimos[:8]}  # Tomamos los primeros 8 sinónimos
    guardar_json(data, nombre_archivo)
