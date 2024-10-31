print(" ")
print("REYES MEZA ALAN EDUARDO 1207 : 3W")
print(" ")
# diccionario con los creditos de las asignaturas
creditos_asignaturas = {
    'matematicas': 10,
    'ingles': 9,
    'ecosistemas': 10,
    'humanidades': 8,
    'lengua y comunicacion': 8,
    'emplea frameworks': 10
}

# mostrar los creditos de cada asignatura
for asignatura, creditos in creditos_asignaturas.items():
    print(f"{asignatura} tiene {creditos} creditos")

# calcular el numero total de creditos
total_creditos = sum(creditos_asignaturas.values())
print(" ")
print(f"total de creditos del curso: {total_creditos}")
