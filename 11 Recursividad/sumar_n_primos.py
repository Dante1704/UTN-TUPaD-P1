""" Realizar una funcion recursiva que permita
sumar los n primeros valores primos

Propiedad matematica:
Un numero no primo tiene al menos un divisor diferente de 1 y de si mismo
Si un numero n tiene un divisor d tal que d <= sqrt{n}, entonces
n puede expresarse como n = d-k, donde k>sqrt{n}.
Por ejemplo: 
Para n=36, los divisores son 2,3,4,6,9,12,18
y basta comprobar hasta 36=sqrt{36} = 6.
Esto significa que si no encontramos divisores de n
menores o iguales a sqrt{n}, entonces n es primo. """ 

from math import sqrt


def es_primo(num:int):
    max_divisor = int(sqrt(num))
    for i in range(2,max_divisor+1):
        if (num % i == 0):
            return False
    return True

def sumar_n_primos(num:int):
    if (num > 1 and es_primo(num)):
        return num + sumar_n_primos(num-1)
    elif (num >= 1):
        return sumar_n_primos(num-1)
    else:
        return num
    
print(sumar_n_primos(5))