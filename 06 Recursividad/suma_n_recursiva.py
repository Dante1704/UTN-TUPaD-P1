def suma_n_recursiva(num:int):
    if num == 0:
        return 0
    else:
        return num + suma_n_recursiva(num - 1)
    
print(suma_n_recursiva(100))