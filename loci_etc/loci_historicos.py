#loci_historicos.py


import json

# Lista de personajes asociados a los primeros 16 hexagramas del I Ching
hexagramas = {
    1: {"nombre": "El Cielo", "personaje": "Leonardo Da Vinci"},
    2: {"nombre": "La Tierra", "personaje": "Isaac Newton"},
    3: {"nombre": "Dificultad Inicial", "personaje": "Arquímedes"},
    4: {"nombre": "Juventud", "personaje": "Sócrates"},
    5: {"nombre": "La Espera", "personaje": "Nikola Tesla"},
    6: {"nombre": "Conflicto", "personaje": "Alejandro Magno"},
    7: {"nombre": "El Ejército", "personaje": "Julio César"},
    8: {"nombre": "Solidaridad", "personaje": "Jesús de Nazaret"},
    9: {"nombre": "La Pequeña Fuerza", "personaje": "Miguel Ángel"},
    10: {"nombre": "El Porte", "personaje": "Confucio"},
    11: {"nombre": "La Paz", "personaje": "Buda"},
    12: {"nombre": "El Estancamiento", "personaje": "René Descartes"},
    13: {"nombre": "La Comunidad con los Hombres", "personaje": "Moisés"},
    14: {"nombre": "La Gran Posesión", "personaje": "Albert Einstein"},
    15: {"nombre": "La Modestia", "personaje": "San Francisco de Asís"},
    16: {"nombre": "El Entusiasmo", "personaje": "Thomas Edison"}
}

# Continuación de la lista de personajes asociados a los hexagramas del I Ching
hexagramas.update({
    17: {"nombre": "El Seguimiento", "personaje": "Pitágoras"},
    18: {"nombre": "La Corrección de lo Corrompido", "personaje": "Hércules"},
    19: {"nombre": "Acercamiento", "personaje": "Platón"},
    20: {"nombre": "La Contemplación", "personaje": "Hipatia de Alejandría"},
    21: {"nombre": "La Mordedura Tajante", "personaje": "Aquiles"},
    22: {"nombre": "La Gracia", "personaje": "Pericles"},
    23: {"nombre": "El Desmoronamiento", "personaje": "Zeus"},
    24: {"nombre": "El Retorno", "personaje": "Ulises"},
    25: {"nombre": "La Inocencia", "personaje": "San Pedro"},
    26: {"nombre": "La Fuerza Educativa de lo Grande", "personaje": "Solón"},
    27: {"nombre": "Las Comisuras de los Labios", "personaje": "Demócrito"},
    28: {"nombre": "La Preponderancia de lo Grande", "personaje": "Gengis Kan"},
    29: {"nombre": "Lo Abismal", "personaje": "Hannibal"},
    30: {"nombre": "El Fuego", "personaje": "Prometeo"},
    31: {"nombre": "La Influencia", "personaje": "Cleopatra"},
    32: {"nombre": "La Duración", "personaje": "Hammurabi"}
})

# Continuación de la lista de personajes asociados a los hexagramas del I Ching
hexagramas.update({
    33: {"nombre": "La Retirada", "personaje": "Sun Tzu"},
    34: {"nombre": "El Poder de lo Grande", "personaje": "Alejandro Magno"},
    35: {"nombre": "El Progreso", "personaje": "Leonidas de Esparta"},
    36: {"nombre": "El Oscurecimiento de la Luz", "personaje": "Edgar Allan Poe"},
    37: {"nombre": "El Clan", "personaje": "Carlomagno"},
    38: {"nombre": "La Oposición", "personaje": "Héctor de Troya"},
    39: {"nombre": "El Obstáculo", "personaje": "Job"},
    40: {"nombre": "La Liberación", "personaje": "Simón Bolívar"},
    41: {"nombre": "La Pérdida", "personaje": "Marco Antonio"},
    42: {"nombre": "El Aumento", "personaje": "Ciro el Grande"},
    43: {"nombre": "El Desbordamiento", "personaje": "Ramsés II"},
    44: {"nombre": "El Encontrarse", "personaje": "Atenea"},
    45: {"nombre": "La Reunión", "personaje": "Juana de Arco"},
    46: {"nombre": "El Ascenso", "personaje": "Salomón"},
    47: {"nombre": "La Angustia", "personaje": "Sísifo"},
    48: {"nombre": "El Pozo", "personaje": "Pitágoras"}
})

# Continuación de la lista de personajes asociados a los hexagramas del I Ching
hexagramas.update({
    49: {"nombre": "La Revolución", "personaje": "Napoleón Bonaparte"},
    50: {"nombre": "El Caldero", "personaje": "Moisés"},
    51: {"nombre": "La Conmoción", "personaje": "Thor"},
    52: {"nombre": "La Inmovilidad", "personaje": "Buda"},
    53: {"nombre": "El Desarrollo", "personaje": "Leonardo da Vinci"},
    54: {"nombre": "La Doncella", "personaje": "Afrodita"},
    55: {"nombre": "La Abundancia", "personaje": "Constantino el Grande"},
    56: {"nombre": "El Andariego", "personaje": "Marco Polo"},
    57: {"nombre": "Lo Penetrante", "personaje": "Eolo"},
    58: {"nombre": "La Serenidad", "personaje": "Teresa de Calcuta"},
    59: {"nombre": "La Disolución", "personaje": "Nostradamus"},
    60: {"nombre": "La Moderación", "personaje": "Confucio"},
    61: {"nombre": "La Verdad Interior", "personaje": "Sófocles"},
    62: {"nombre": "La Pequeñez en lo Grande", "personaje": "Isaac Newton"},
    63: {"nombre": "Después de la Consumación", "personaje": "Hércules"},
    64: {"nombre": "Antes de la Consumación", "personaje": "Hammurabi"}
})

# Lista de personajes asociados a los hexagramas del I Ching sin repeticiones
hexagramas = {
    1: {"nombre": "El Cielo", "personaje": "Leonardo Da Vinci"},
    2: {"nombre": "La Tierra", "personaje": "Isaac Newton"},
    3: {"nombre": "Dificultad Inicial", "personaje": "Arquímedes"},
    4: {"nombre": "Juventud", "personaje": "Sócrates"},
    5: {"nombre": "La Espera", "personaje": "Nikola Tesla"},
    6: {"nombre": "Conflicto", "personaje": "Alejandro Magno"},
    7: {"nombre": "El Ejército", "personaje": "Julio César"},
    8: {"nombre": "Solidaridad", "personaje": "Jesús de Nazaret"},
    9: {"nombre": "La Pequeña Fuerza", "personaje": "Miguel Ángel"},
    10: {"nombre": "El Porte", "personaje": "Confucio"},
    11: {"nombre": "La Paz", "personaje": "Buda"},
    12: {"nombre": "El Estancamiento", "personaje": "René Descartes"},
    13: {"nombre": "La Comunidad con los Hombres", "personaje": "Moisés"},
    14: {"nombre": "La Gran Posesión", "personaje": "Albert Einstein"},
    15: {"nombre": "La Modestia", "personaje": "San Francisco de Asís"},
    16: {"nombre": "El Entusiasmo", "personaje": "Thomas Edison"},
    17: {"nombre": "El Seguimiento", "personaje": "Pitágoras"},
    18: {"nombre": "La Corrección de lo Corrompido", "personaje": "Sófocles"},
    19: {"nombre": "Acercamiento", "personaje": "Platón"},
    20: {"nombre": "La Contemplación", "personaje": "Hipatia de Alejandría"},
    21: {"nombre": "La Mordedura Tajante", "personaje": "Aquiles"},
    22: {"nombre": "La Gracia", "personaje": "Pericles"},
    23: {"nombre": "El Desmoronamiento", "personaje": "Zeus"},
    24: {"nombre": "El Retorno", "personaje": "Ulises"},
    25: {"nombre": "La Inocencia", "personaje": "San Pedro"},
    26: {"nombre": "La Fuerza Educativa de lo Grande", "personaje": "Solón"},
    27: {"nombre": "Las Comisuras de los Labios", "personaje": "Demócrito"},
    28: {"nombre": "La Preponderancia de lo Grande", "personaje": "Gengis Kan"},
    29: {"nombre": "Lo Abismal", "personaje": "Hannibal"},
    30: {"nombre": "El Fuego", "personaje": "Prometeo"},
    31: {"nombre": "La Influencia", "personaje": "Cleopatra"},
    32: {"nombre": "La Duración", "personaje": "Hammurabi"},
    33: {"nombre": "La Retirada", "personaje": "Sun Tzu"},
    34: {"nombre": "El Poder de lo Grande", "personaje": "Aníbal Barca"},
    35: {"nombre": "El Progreso", "personaje": "Leonidas de Esparta"},
    36: {"nombre": "El Oscurecimiento de la Luz", "personaje": "Edgar Allan Poe"},
    37: {"nombre": "El Clan", "personaje": "Carlomagno"},
    38: {"nombre": "La Oposición", "personaje": "Héctor de Troya"},
    39: {"nombre": "El Obstáculo", "personaje": "Job"},
    40: {"nombre": "La Liberación", "personaje": "Simón Bolívar"},
    41: {"nombre": "La Pérdida", "personaje": "Marco Antonio"},
    42: {"nombre": "El Aumento", "personaje": "Ciro el Grande"},
    43: {"nombre": "El Desbordamiento", "personaje": "Ramsés II"},
    44: {"nombre": "El Encontrarse", "personaje": "Atenea"},
    45: {"nombre": "La Reunión", "personaje": "Juana de Arco"},
    46: {"nombre": "El Ascenso", "personaje": "Salomón"},
    47: {"nombre": "La Angustia", "personaje": "Sísifo"},
    48: {"nombre": "El Pozo", "personaje": "Heródoto"},
    49: {"nombre": "La Revolución", "personaje": "Napoleón Bonaparte"},
    50: {"nombre": "El Caldero", "personaje": "Zaratustra"},
    51: {"nombre": "La Conmoción", "personaje": "Thor"},
    52: {"nombre": "La Inmovilidad", "personaje": "Lao-Tsé"},
    53: {"nombre": "El Desarrollo", "personaje": "Hipócrates"},
    54: {"nombre": "La Doncella", "personaje": "Afrodita"},
    55: {"nombre": "La Abundancia", "personaje": "Constantino el Grande"},
    56: {"nombre": "El Andariego", "personaje": "Marco Polo"},
    57: {"nombre": "Lo Penetrante", "personaje": "Eolo"},
    58: {"nombre": "La Serenidad", "personaje": "Teresa de Calcuta"},
    59: {"nombre": "La Disolución", "personaje": "Nostradamus"},
    60: {"nombre": "La Moderación", "personaje": "Confucio"},
    61: {"nombre": "La Verdad Interior", "personaje": "Avicena"},
    62: {"nombre": "La Pequeñez en lo Grande", "personaje": "Florence Nightingale"},
    63: {"nombre": "Después de la Consumación", "personaje": "Hércules"},
    64: {"nombre": "Antes de la Consumación", "personaje": "Homero"}
}



# Guardar los datos en un archivo JSON
with open('../json/loci_historicos.json', 'w') as file:
    json.dump(hexagramas, file, indent=4, ensure_ascii=False)

print("Archivo JSON generado con éxito.")

