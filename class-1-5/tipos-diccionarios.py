# Los diccionarios definen los datos uno a uno entre un campo y un valor

datos_basicos = {
    "name": "Madeline",
    "apellidos": "Aviles",
    "Edad": 21,
    "Numero identidad": "034567878",
    "Estado civil": "casada"
}
print("Detalle del diccionario creado:")
print("===============================\n")
print("Claves del diccionario: ", datos_basicos.keys())
print("Valores del diccionario:", datos_basicos.values())
print("Elementos del diccionario:", datos_basicos.items())

# Ejemplo practico de los diccionarios
print("Inscripcion de Estudiante")
print("-------------------------\n")
print("Documento de identidad:",datos_basicos['Numero identidad'])
print("Nombre completo:", datos_basicos['name'], datos_basicos["apellidos"])
