# Crear un diccionario
informacion_personal = {
    "nombre": "fernanda",
    "edad": 28,
    "ciudad": "Guayaquil",
    "profesion": "Tecnologa"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Desarrollador"

# Verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0969983856"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
