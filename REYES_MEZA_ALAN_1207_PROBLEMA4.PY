# diccionario para almacenar la informacion personal
informacion_personal = {}

# preguntar al usuario su nombre, edad, direccion y telefono
informacion_personal['nombre'] = input("introduce tu nombre: ")
informacion_personal['edad'] = input("introduce tu edad: ")
informacion_personal['direccion'] = input("introduce tu direccion: ")
informacion_personal['telefono'] = input("introduce tu numero de telefono: ")

# mostrar la informacion en el formato deseado
print(f"{informacion_personal['nombre']} tiene {informacion_personal['edad']} años, vive en {informacion_personal['direccion']} y su numero de telefono es {informacion_personal['telefono']}.")