def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese aquí el nombre del compañero: ")
        edad = int(input("Ingrese aquí la edad del compañero: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    
    compañeros.sort(key=lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    # Lista para almacenar los nombres de todos los compañeros
    lista_nombres = [nombre for nombre, _ in compañeros]
    print("Nombres de todos los compañeros:", lista_nombres)
    
    return asistente, profesor

asistente, profesor = obtener_compañeros(5)
print("El asistente más joven es:", asistente)
print("El profesor más viejo es:", profesor)



