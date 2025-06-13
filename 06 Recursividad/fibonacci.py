'''Calcula el valor de Fibonacci en la posicion dada
en forma recursiva
:param pos: Posicion en la secuencia de Fibonacci (debe ser >= 0).
:return: Valor de Fibonacci en al posicion indicada.
'''

def fibonacci(pos:int):
    if (pos == 1):
        return 1
    elif (pos == 0):
        return 0
    else:
        return fibonacci(pos - 2) + fibonacci(pos - 1)     

print(fibonacci(4))