# Ej 5 
contrasena = input("Ingrese la contraseña entre 8 - 14 carateres: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Contraseña correcta")
else:
    print("Por favor ingrese una contraseña entre 8 - 14 caracteres")

# Ej 6 
from statistics import mode, median, mean

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")

 # Ej 7
frase = input("Ingrese una frase o palabra: ")
if frase.endswith(('a', 'e', 'i', 'o', 'u')):
    frase = frase + '!'
else:  
    pass
print(frase)

# Ej 8
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese uno de los siguientes numeros: \n 1- Si quiere su nombre en mayusculas \n 2- Si quiere su nombre en minusculas \n 3- Si quiere su nombre en capitalizada"))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.capitalize())
else:  
    print("Opcion no valida")


# Ej 9
magnitud = float(input("Ingrese la magnitud del sismo: "))
if magnitud < 0:
    print("Magnitud no valida")
elif magnitud < 3.0:
    print("Muy Leve")
elif magnitud >= 3.0 and magnitud < 4.0:
    print("Leve")
elif magnitud >= 4.0 and magnitud < 5.0:
    print("Moderado")
elif magnitud >= 5.0 and magnitud < 6.0:
    print("Fuerte")
elif magnitud >= 6.0 and magnitud < 7.0:
    print("Muy Fuerte")
else :
    print("Extremo")


    