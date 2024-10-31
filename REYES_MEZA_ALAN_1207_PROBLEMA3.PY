print(" ")
print("REYES MEZA ALAN EDUARDO 1207 : 3W")
print(" ")
# lista de asignaturas
asignaturas = ["matematicas", "humanidades", "ecosistemas", "emplea frameworks", "lengua y comunicacion"]

# diccionario para almacenar las notas
notas = {}

# preguntar al usuario la nota de cada asignatura
for asignatura in asignaturas:
    while True:
        try:
            nota = float(input(f"introduce la calif de {asignatura}: "))
            if 0 <= nota <= 10:  # asumiendo que la nota esta entre 0 y 10
                notas[asignatura] = nota
                break
            else:
                print("la calif debe estar entre 0 y 10. corrigelo")
        except ValueError:
            print("introduce tu calif correctamente")

# mostrar las notas
for asignatura, nota in notas.items():
    print(" ")
    print(f"en {asignatura} has sacado {nota}")
    print(" ")


