# Ejemplo de tuplas para una conexion a una base de datos

print("Conectando a una base de datos de MySQL")
print("========================================\n")

conexion_db = "192.168.0.61", "root", "password_root", "example_db"
print("Conexion tipica:", conexion_db)
print(conexion_db)

conexion_c = conexion_db, "3306", "30"
print("\nConexion con estos parametros", conexion_c)
print(conexion_c)

print("Acceder a la IP de la base de datos:", conexion_c[0][0])
print("Acceder al usuario de la base de datos:", conexion_c[0][1])
print("Acceder al nombre de la base de datos:", conexion_c[0][3])
print("Acceder al puerto de conexion:", conexion_c[1])
print("Acceder al tiempo de espera de la conexion:", conexion_c[2])