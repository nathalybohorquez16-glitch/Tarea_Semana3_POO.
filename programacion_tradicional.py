# ==================================================
# Sistema de Gestión de Mascotas
# Programación Tradicional
# Estudiante: Daniela Gómez
# ==================================================

# Función para registrar los datos de una mascota
def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))

    return nombre, especie, edad


# Función para mostrar la información de la mascota
def mostrar_mascota(nombre, especie, edad):
    print("\n--- INFORMACIÓN DE LA MASCOTA ---")
    print(f"Nombre : {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad   : {edad} años")


# Programa principal
nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)
