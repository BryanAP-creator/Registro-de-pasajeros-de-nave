#Bryan Angulo Portuguez
#Registro de pasajeros

# Definimos el tamaño de la aeronave: 5 filas y 4 asientos por fila.
FILAS = 5
ASIENTOS_POR_FILA = 4

# Creamos una matriz que representa los asientos. Inicialmente, todos están "Vacío".
aeronave = [["Vacío" for _ in range(ASIENTOS_POR_FILA)] for _ in range(FILAS)]


# Función para asignar un pasajero a un asiento específico
def asignar_asiento(fila, asiento, nombre):
    if 0 <= fila < FILAS and 0 <= asiento < ASIENTOS_POR_FILA:
        if aeronave[fila][asiento] == "Vacío":
            aeronave[fila][asiento] = nombre
            print(f"Asiento {fila + 1}{asiento + 1} asignado a {nombre}.")
        else:
            print(f"El asiento {fila + 1}{asiento + 1} ya está ocupado por {aeronave[fila][asiento]}.")
    else:
        print("Número de fila o asiento no válido.")


# Función para imprimir todos los asientos y su estado
def imprimir_asientos():
    for i in range(FILAS):
        for j in range(ASIENTOS_POR_FILA):
            print(f"Asiento {i + 1}{j + 1}: {aeronave[i][j]}")
        print("-" * 20)


# Función para consultar un asiento específico
def consultar_asiento(fila, asiento):
    if 0 <= fila < FILAS and 0 <= asiento < ASIENTOS_POR_FILA:
        print(f"Asiento {fila + 1}{asiento + 1}: {aeronave[fila][asiento]}")
    else:
        print("Número de fila o asiento no válido.")


# Ejemplo de uso del programa
while True:
    print("\nMenú:")
    print("1. Asignar asiento")
    print("2. Consultar asiento")
    print("3. Imprimir todos los asientos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        fila = int(input("Ingrese el número de fila (1-5): ")) - 1
        asiento = int(input("Ingrese el número de asiento (1-4): ")) - 1
        nombre = input("Ingrese el nombre del pasajero: ")
        asignar_asiento(fila, asiento, nombre)

    elif opcion == "2":
        fila = int(input("Ingrese el número de fila (1-5): ")) - 1
        asiento = int(input("Ingrese el número de asiento (1-4): ")) - 1
        consultar_asiento(fila, asiento)

    elif opcion == "3":
        imprimir_asientos()

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")