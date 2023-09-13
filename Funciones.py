def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range (cantidad_de_compañeros):
        nombre = input("Ingrese aquí el nonmbre del compañero: ")
        edad = int(input("Ingrese aquí la edad del compañero: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros [-1][0]
    #Lista = []
    #print(lista[])
    return asistente, profesor
    
    
obtener_compañeros(3)
