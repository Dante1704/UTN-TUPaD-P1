'''pasando una lista de numeros, 
obtener la suma total de los mismos de forma recursiva'''

def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

lista = [1,2,3,4,5]
print(f'la suma es: {sum_list(lista)}')