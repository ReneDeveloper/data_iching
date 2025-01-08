#sinonimos_01_16.py

import jsonC
import os

# Sinónimos únicos de los hexagramas del 1 al 16 con al menos 8 sinónimos
sinonimos_hexagramas = {
    "01": ["Creativo", "Cielo", "Creador", "Fuerza Creativa", "Innovación", "Originalidad", "Inspiración", "Creación"],
    "02": ["Receptivo", "Tierra", "Sumisión", "Devoción", "Acogida", "Firmeza", "Lealtad", "Tolerancia"],
    "03": ["Dificultad Inicial", "Comienzo Difícil", "Iniciativa", "Desafío", "Problema", "Contrariedad", "Desventaja", "Adversidad"],
    "04": ["Juventud", "Inmadurez", "Joven", "Aprendiz", "Novato", "Novedoso", "Principiante", "Inexperiencia"],
    "05": ["Espera", "Expectativa", "Esperanza", "Anticipación", "Paciencia", "Previsión", "Aguardo", "Expectación"],
    "06": ["Conflicto", "Disputa", "Pleito", "Contienda", "Pugna", "Rivalidad", "Competencia", "Enfrentamiento"],
    "07": ["Ejército", "Multitud", "Grupo", "Reunión", "Agregación", "Conjunto", "Comunidad", "Horda"],
    "08": ["Solidaridad", "Unión", "Cohesión", "Alianza", "Colectividad", "Cooperación", "Conjunción", "Compromiso"],
    "09": ["Poder de lo Pequeño", "Poder de lo Manso", "Fuerza Interior", "Resistencia", "Humildad", "Modestia", "Sencillez", "Docilidad"],
    "10": ["Tensión", "Marcha", "Paso", "Conducta", "Movimiento", "Agitación", "Acción", "Proceder"],
    "11": ["Paz", "Tranquilidad", "Estancamiento", "Satisfacción", "Estabilidad", "Plenitud", "Equilibrio", "Contentamiento"],
    "12": ["Obstrucción", "Caída de lo Grande", "Bloqueo", "Impedimento", "Traba", "Estorbo", "Contratiempo", "Adversidad"],
    "13": ["Comunidad con los Hombres", "Unión Comunitaria", "Hermandad con los Hombres", "Solidaridad", "Humanidad", "Compañerismo", "Fraternidad", "Colectividad"],
    "14": ["Gran Posesión", "Gran Abundancia", "Riqueza", "Opulencia", "Abundancia", "Fartura", "Prosperidad", "Riquezas"],
    "15": ["Moderación", "Humildad", "Sencillez", "Mesura", "Discreción", "Sobriedad", "Contención", "Recato"],
    "16": ["Entusiasmo", "Alegría", "Excitación", "Energía", "Vigor", "Fervor", "Júbilo", "Emoción"]
}

# Ruta base donde se guardarán los archivos JSON
ruta_base = '../json/'

# Función para guardar el archivo JSON
def guardar_json(data, nombre_archivo):
    ruta_archivo = os.path.join(ruta_base, nombre_archivo)
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Archivo '{ruta_archivo}' creado con éxito.")

# Guardar cada archivo JSON para los 16 primeros hexagramas
for numero_hexagrama, sinonimos in sinonimos_hexagramas.items():
    nombre_archivo = f'sinonimos_{numero_hexagrama}.json'
    data = {numero_hexagrama: sinonimos[:8]}  # Tomamos los primeros 8 sinónimos
    guardar_json(data, nombre_archivo)
