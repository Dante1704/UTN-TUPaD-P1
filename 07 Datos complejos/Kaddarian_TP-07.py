import re

#Ej 1 2 3

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450}

# precios_frutas["Naranja"] = 1200
# precios_frutas["Manzana"] = 1500
# precios_frutas["Pera"] = 2300

# print(precios_frutas.items())

# precios_frutas["Banana"] = 1330
# precios_frutas["Manzana"] = 1700
# precios_frutas["Melón"] = 2800

# print(precios_frutas.items())

# frutas = [*precios_frutas.keys()]

# print(frutas)

#Ej 4

# guia_telefonica= {}

# for i in range(0,5):
#     nombre = input("Ingrese un nombre: ")
#     telefono = input("Ingrese el teléfono: ")
#     guia_telefonica[nombre] = telefono

# print(guia_telefonica.items())

#Ej 5

# frase = input("ingrese una frase: ")
# palabras = re.split(r'[\s\W]+', frase)
# palabras = [p for p in palabras if p] #filtra elementos vacios
# palabras_unicas = {*palabras}

# print(palabras_unicas)

#Ej 6

# alumnos = {}

# for i in range(0,3):
#     notas = []
#     nombre = input("Ingrese un nombre: ")
#     for j in range(0,3):
#         notas.append(int(input("ingrese una nota: ")))
#     alumnos[nombre] = tuple(notas)

# print(alumnos.items())

#Ej 7

#Ej 8

# productos = {
#     "manzanas": 50,
#     "bananas": 30,
#     "leche": 20,
#     "pan": 15,
#     "queso": 10
# }

# def consultar_stock():
#     producto = input("Ingrese el nombre del producto a consultar: ")
#     if producto in productos:
#         print(f"El stock de {producto} es: {productos[producto]}")
#     else:
#         print("Producto no encontrado.")

# def agregar_stock():
#     producto = input("Ingrese el nombre del producto a agregar: ")
#     cantidad = int(input("Ingrese la cantidad a agregar: "))
#     if producto in productos:
#         productos[producto] += cantidad
#     else:
#         print("Producto no encontrado.")

# def agregar_producto():
#     producto = input("Ingrese el nombre del producto a agregar: ")
#     cantidad = int(input("Ingrese la cantidad del producto: "))
#     if producto in productos:
#         print("El producto ya existe. No se puede agregar.")
#     else:
#         productos[producto] = cantidad
#         print(f"Producto {producto} agregado con cantidad {cantidad}.")

# def menu():
#     while True:
#         print("\nMenú de opciones:")
#         print("1. Consultar stock")
#         print("2. Agregar stock a un producto existente")
#         print("3. Agregar un nuevo producto")
#         print("4. Salir")
        
#         opcion = input("Seleccione una opción: ")
        
#         if opcion == "1":
#             consultar_stock()
#         elif opcion == "2":
#             agregar_stock()
#         elif opcion == "3":
#             agregar_producto()
#         elif opcion == "4":
#             print("Saliendo del programa.")
#             break
#         else:
#             print("Opción no válida, intente nuevamente.")

# menu()

#Ej 10

# paises_capitales = {
#     "Argentina": "Buenos Aires",
#     "Brasil": "Brasilia",
#     "Chile": "Santiago",
#     "Colombia": "Bogotá",
#     "Perú": "Lima"
# }

# capitales_paises = {}
# for pais, capital in paises_capitales.items():
#     capitales_paises[capital] = pais
# print("Diccionario de capitales y países:")
# print(capitales_paises.items())