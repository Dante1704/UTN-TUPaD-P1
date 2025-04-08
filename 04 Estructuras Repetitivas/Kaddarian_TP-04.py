# Ej 2

# numero = input("ingrese un numero entero: ")
# digitos = len(numero)
# print(f"el numero {numero} tiene {digitos} digitos")

# Ej 5

# import random

# intentos = 0
# numero = 0
# numeroRandom = 1

# while numero != numeroRandom: 
#     intentos += 1
#     numeroRandom = random.randint(0,9)
#     numero = int(input("Ingrese un numero entero entre 0 y 9: "))
#     if numeroRandom == numero:
#         print(f"Felicidades! Acertaste el numero en {intentos} intentos")
    

# Ej 8

# positivos = 0
# negativos = 0
# pares = 0
# impares = 0
# for i in range(10): 
#     numero = int(input("Ingrese un numero entero: "))
#     if (numero > 0):
#         positivos += 1
#     if numero < 0:
#         negativos += 1
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares +=1
# print(f"pares: {pares}, impares: {impares}, positivos: {positivos}, negativos: {negativos}")

# Ej 10

numero = input("ingrese un numero para invertirlo: ")
numeroInvertido = ''
esNegativo = False
if(numero[0] == '-'):
    esNegativo = True

index = len(numero) - 1
print(f"index: {index}")

while index >= 0 :
    if esNegativo and index == 0:
        numeroInvertido = numero[index] + numeroInvertido
        index -= 1
    else: 
        numeroInvertido += numero[index]
        index -= 1
print(f"numero invertido: {numeroInvertido}")
    