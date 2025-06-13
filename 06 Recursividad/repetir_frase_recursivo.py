'''Realizar una funcion recursiva
que reciba un numero y una frase y la 
repita el numero de veces ingresado'''


def repetir_frase_recursivo(frase:str, rep:int):
    if rep == 0:
        return frase
    else:
        print(frase)
        return repetir_frase_recursivo(frase, rep - 1)
    return

repetir_frase_recursivo("hola mundo", 5)