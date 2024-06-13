numeros = []
while True:
    numeron = float(input("Ingrese una numero (o '0' para terminar): "))
    if numeron == 0:
        break
    numeros.append(numeron)
    sumatoria = sum(numeros)
    print(sumatoria)
    print(f"Los numeros sumados fueron: {numeros}")
    promedio = sumatoria/len(numeros)
    print(F"EL PROMEDIO DE ESTA SUMA ES: {promedio}")
