datos_personales = {
    "nombre": "Juan",
    "edad": 30,
    "caracteristicas": ["analítico", "observador", "optimista", "adaptable"],
    "ubicacion": "Zona Colonial, República Dominicana"
}

print("Datos personales:")
print(f"Nombre: {datos_personales['nombre']}")
print(f"Edad: {datos_personales['edad']} años")
print(f"Características: {', '.join(datos_personales['caracteristicas'])}")
print(f"Ubicación: {datos_personales['ubicacion']}")

aja = int(input("Desea agregar algun dato?: Si=1  No=0 "))
if aja == 1:
    datonuevo = input("Escribelo aqui:")
    datos_personales['Datos adicionales'] = datonuevo
else:
    print("Gracias de todos modos")

print("Estos son los datos actualizados:")
print(datos_personales)
