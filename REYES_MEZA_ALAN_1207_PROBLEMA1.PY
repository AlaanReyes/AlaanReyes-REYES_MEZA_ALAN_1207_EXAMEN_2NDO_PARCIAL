print(" ")
print("REYES MEZA ALAN EDUARDO 1207 : 3W")
print(" ")
# lista de asignaturas en curso
asignaturas = ["matematicas", "ingles", "ecosistemas", "humanidades", "lengua y comunicacion", "emplea frameworks"]

# diccionario para almacenar las notas de asignaturas
notas = {}

# preguntar al usuario la nota de cada asignatura
for asignatura in asignaturas:
    while True:
        try:
            nota = float(input(f"introduce la calif de {asignatura}: "))
            if 0 <= nota <= 10:  #la calif debe estar entre 0 y 10
                notas[asignatura] = nota
                break
            else:
                print("la calif debe estar entre 0 y 10. introduce tu calif correctamente")
        except ValueError:
            print("por favor, introduce tu calif correctamente")

# eliminar asignaturas aprobadas
asignaturas_repetir = [asignatura for asignatura in asignaturas if notas[asignatura] < 6]

# mostrar las asignaturas que el usuario tiene que repetir
if asignaturas_repetir:
    print(" ")
    print("Asignaturas que tienes que repetir:")
    for asignatura in asignaturas_repetir:
        print(asignatura)
else:
    print(" ")
    print("¡Felicitaciones has logrado aprobar todas tus asignaturas!")

