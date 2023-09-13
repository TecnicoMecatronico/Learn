def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        while True:
            nombre = input("Ingrese aquí el nombre del compañero: ")
            if nombre.isalpha():
                break
            else:
                print("El nombre no es correcto. Debe ser una cadena.")
        while True:
            edad = input("Ingrese aquí la edad del compañero: ")
            # Validación para asegurarse de que se ingresó un número entero.
            if edad.isdigit():
                compañero = (nombre, edad)
                compañeros.append(compañero)
                break  # Salir del ciclo si los valores son válidos
            else:
                print("La edad debe ser un número entero positivo")
    compañeros.sort(key=lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    lista_nombres = [nombre for nombre, _ in compañeros]
    print("Nombres de todos los compañeros:", lista_nombres)
    return asistente, profesor


asistente, profesor = obtener_compañeros(3)


print("El asistente más joven es:", asistente)
print("El profesor más viejo es:", profesor)
