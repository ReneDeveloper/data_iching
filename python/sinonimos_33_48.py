#sinonimos_33_48.py

import json
import os

# Sinónimos únicos de los hexagramas del 33 al 48 con al menos 8 sinónimos
sinonimos_hexagramas = {
    "33": ["Retirada", "Retorno", "Repliegue", "Retiro", "Abandono", "Retorno", "Reversión", "Vuelta"],
    "34": ["Gran Fuerza", "Gran Poder", "Gran Energía", "Gran Intensidad", "Gran Vitalidad", "Gran Potencia", "Gran Fortaleza", "Gran Pujanza"],
    "35": ["Progresión", "Avance", "Desarrollo", "Evolución", "Crecimiento", "Mejora", "Adelanto", "Ascenso"],
    "36": ["Oscurecimiento", "Oscuridad", "Ocultamiento", "Encubrimiento", "Confusión", "Desorientación", "Enmascaramiento", "Velamiento"],
    "37": ["Casa del Clan", "Casa de la Familia", "Casa del Hijo Menor", "Casa de la Familia Joven", "Residencia", "Moradia", "Vivienda", "Domicilio"],
    "38": ["Oposición", "Contradicción", "Antagonismo", "Resistencia", "Conflicto", "Enfrentamiento", "Disputa", "Pugna"],
    "39": ["Dificultad", "Obstáculo", "Desafío", "Problema", "Adversidad", "Contratiempo", "Contrariedad", "Complicación"],
    "40": ["Liberación", "Desatar", "Soltar", "Desprender", "Desvincular", "Separar", "Desligar", "Libertad"],
    "41": ["Disminución", "Decremento", "Reducción", "Merma", "Menoscabo", "Mengua", "Disminución", "Declinación"],
    "42": ["Incremento", "Aumento", "Crecimiento", "Ampliación", "Expansión", "Desarrollo", "Fortalecimiento", "Avance"],
    "43": ["Determinación", "Decisión", "Resolución", "Conclusión", "Firmeza", "Definición", "Decisión", "Determinación"],
    "44": ["Acoplamiento", "Reunión", "Encuentro", "Reconciliación", "Unión", "Convergencia", "Enlace", "Conexión"],
    "45": ["Reunión", "Congregación", "Agrupación", "Asamblea", "Encuentro", "Confluencia", "Concentración", "Reunión"],
    "46": ["Ascenso", "Auge", "Crecimiento", "Elevación", "Subida", "Incremento", "Progreso", "Desarrollo"],
    "47": ["Oprimir", "Agotar", "Exhaustar", "Debilitar", "Aplastar", "Someter", "Sobrecargar", "Exigir"],
    "48": ["El Pozo", "La Fuente", "El Origen", "La Cisterna", "Manantial", "Nacimiento", "Vertiente", "Nacimiento"]
}

# Ruta base donde se guardarán los archivos JSON
ruta_base = '../json/'

# Función para guardar el archivo JSON
def guardar_json(data, nombre_archivo):
    ruta_archivo = os.path.join(ruta_base, nombre_archivo)
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Archivo '{ruta_archivo}' creado con éxito.")

# Guardar cada archivo JSON para los hexagramas del 33 al 48
for numero_hexagrama, sinonimos in sinonimos_hexagramas.items():
    nombre_archivo = f'sinonimos_{numero_hexagrama}.json'
    data = {numero_hexagrama: sinonimos[:8]}  # Tomamos los primeros 8 sinónimos
    guardar_json(data, nombre_archivo)
