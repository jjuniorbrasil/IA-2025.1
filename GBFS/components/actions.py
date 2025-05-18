actions = {
    'Arad': [('Zerind', 75), ('Sibiu', 140),('Timisoara', 118)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
    'Bucharest': [('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90)]
}

actionsNE = {
    'São Luís': [('Teresina', 446), ('Fortaleza', 1075)],
    'Teresina': [('São Luís', 446), ('Fortaleza', 636), ('Picos', 310)],
    'Fortaleza': [('Teresina', 636), ('São Luís', 1075), ('Natal', 537)],
    'Picos': [('Teresina', 310), ('Juazeiro do Norte', 362)],
    'Juazeiro do Norte': [('Picos', 362), ('Campina Grande', 509)],
    'Natal': [('Fortaleza', 537), ('João Pessoa', 185)],
    'João Pessoa': [('Natal', 185), ('Campina Grande', 120), ('Recife', 120)],
    'Campina Grande': [('Juazeiro do Norte', 509), ('João Pessoa', 120)],
    'Recife': [('João Pessoa', 120)]
}

straigth_line_distance_to_bucharest_from = {
    'Arad': 366,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374,
    'Fagaras': 176,
    'Oradea': 380,
    'Rimnicu Vilcea': 193,
    'Bucharest': 0,
}