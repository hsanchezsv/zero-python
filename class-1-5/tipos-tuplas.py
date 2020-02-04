# Las tuplas son listas que no se pueden modificar despues de su creacion.
# son inmodificables

# ejemplo simple
tupla = 1965, 59621, "hola, Python."
print(tupla)

otra = tupla, (1, 5, 3, 6, 5)
print(otra)

# operacion asignacion de valores de una tupla en variables
x, y, z = tupla
print(x, y, z)

