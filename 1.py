cadenas = []
while True:
    palabran = input("Ingrese una palabra (o 'salir' para terminar): ")
    if palabran == 'salir':
        break
    cadenas.append(palabran)
    print(f"Todas las palabras introducidas: {cadenas}")
    longitud_mayor_que_4 = [cadena for cadena in cadenas if len(cadena) > 4]
    print(f"Palabras de mas de 4 letras: {longitud_mayor_que_4}")
