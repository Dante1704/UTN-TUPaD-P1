import utils

#Mostrar si un numero es perfecto o no
#un numero es perfecto si es igual a la suma de sus divisores

#Programa Principal 
#num = utils.leer_entero_validado("Ingrese un número natural", 1)
#informar_si_numero_es_perfecto(num)

#Desarrollar un programa que permita ingresar un ancho y un alto.
#La computadora debe dibujar una matriz de cruces de tales dimensiones.

def imprimir_matriz(ancho, alto):
    for i in range(alto):
        utils.imprimir_simbolo("X", ancho) #el ancho define las columnas
    return

#Programa Principal 
ancho = utils.leer_entero_validado("Ingrese el ancho", 1)
alto = utils.leer_entero_validado("Ingrese el alto", 1)
imprimir_matriz(ancho, alto)