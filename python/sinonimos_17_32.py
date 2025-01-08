#sinonimos_17_32.py

import json
import os

# Sinónimos únicos de los hexagramas del 17 al 32 con al menos 8 sinónimos
sinonimos_hexagramas = {
    "17": ["Seguimiento", "Continuidad", "Consistencia", "Persistencia", "Fidelidad", "Adherencia", "Consecuencia", "Lealtad"],
    "18": ["Reconstrucción", "Renovación", "Corrección", "Mejora", "Rectificación", "Restauración", "Refinamiento", "Perfeccionamiento"],
    "19": ["Aproximación", "Acercamiento", "Encuentro", "Conexión", "Integración", "Unión", "Relación", "Coincidencia"],
    "20": ["Contemplación", "Reflexión", "Meditación", "Concentración", "Consideración", "Observación", "Pensamiento", "Estudio"],
    "21": ["Mordedura", "Desintegración", "Descomposición", "Corrosión", "Deterioro", "Destrucción", "Declive", "Desgaste"],
    "22": ["Gracia", "Encanto", "Atractivo", "Seducción", "Fascinación", "Glamour", "Hechizo", "Atracción"],
    "23": ["Degeneración", "Decadencia", "Deterioro", "Corrupción", "Descomposición", "Desgaste", "Declive", "Desmoronamiento"],
    "24": ["Regreso", "Retorno", "Reversión", "Vuelta", "Restitución", "Repetición", "Reincorporación", "Recuperación"],
    "25": ["Inocencia", "Pureza", "Sencillez", "Ingenuidad", "Candidez", "Simpleza", "Limpieza", "Inocuidad"],
    "26": ["Grandeza", "Majestuosidad", "Nobleza", "Elevación", "Dignidad", "Sublimidad", "Excelencia", "Magnificencia"],
    "27": ["Alimentación", "Nutrición", "Sustento", "Manutención", "Provisión", "Abastecimiento", "Aporte", "Cuidado"],
    "28": ["Excesivo", "Demasiado", "Sobrado", "Superabundante", "Abundante", "Desbordante", "Saturado", "Desmesurado"],
    "29": ["Abismal", "Profundo", "Insondable", "Misterioso", "Enigmático", "Incomprensible", "Indescifrable", "Irracional"],
    "30": ["Fuego Claro", "Claridad", "Luminosidad", "Resplandor", "Brillo", "Radiación", "Iluminación", "Luz"],
    "31": ["Influencia", "Carisma", "Atracción", "Prestigio", "Efecto", "Impacto", "Poder", "Autoridad"],
    "32": ["Duración", "Persistencia", "Permanencia", "Continuidad", "Estabilidad", "Resistencia", "Consistencia", "Constancia"]
}

# Ruta base donde se guardarán los archivos JSON
ruta_base = '../json/'

# Función para guardar el archivo JSON
def guardar_json(data, nombre_archivo):
    ruta_archivo = os.path.join(ruta_base, nombre_archivo)
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Archivo '{ruta_archivo}' creado con éxito.")

# Guardar cada archivo JSON para los hexagramas del 17 al 32
for numero_hexagrama, sinonimos in sinonimos_hexagramas.items():
    nombre_archivo = f'sinonimos_{numero_hexagrama}.json'
    data = {numero_hexagrama: sinonimos[:8]}  # Tomamos los primeros 8 sinónimos
    guardar_json(data, nombre_archivo)
