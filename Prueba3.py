def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        while True:
            nombre = input("Ingrese aquí el nombre del compañero: ")
            if not isinstance(nombre, str):
                print("El nombre no es correcto")
                break
            else:
                break
                
        while True:
            try:
                edad = int(input("Ingrese aquí la edad del compañero: "))
                # Validación para asegurarse de que se ingresó un número entero positivo
                if edad <= 0:
                    raise ValueError("La edad debe ser un número entero positivo")
                
                compañero = (nombre, edad)
                compañeros.append(compañero)
                break  # Salir del ciclo si los valores son válidos
            except ValueError as e:
                print("Error:", e)
    
    compañeros.sort(key=lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    lista_nombres = [nombre for nombre, _ in compañeros]
    print("Nombres de todos los compañeros:", lista_nombres)
    
    return asistente, profesor

asistente, profesor = obtener_compañeros(3)
print("El asistente más joven es:", asistente)
print("El profesor más viejo es:", profesor)
