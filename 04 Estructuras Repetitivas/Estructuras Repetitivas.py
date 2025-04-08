
# for

# for <variable> in range(valor_fin): //el valor_fin no esta includo 
#     <instrucciones> 

for x in range(6):
    print(x, "Debo aprender ciclos")

# for <variable> in range(valor_inicio, valor_fin):
#     <instrucciones> 

for x in range(1, 6):
    print(x, "Arranca en 1 y termina en 5")

# for <variable> in range(valor_inicio, valor_fin, valor_actualizacion): //el valor de actualizacion indica el paso
#     <instrucciones> 

for x in range(11, 1, -1):
    print(x, "Arranca en 11 y termina en 1 y va de 2 en 2")
    

# while

# while <expr_lógica>:
#   <instrucciones a repetir> -> tiene que haber indentado para que se ejecuten en el while

# max y min

# si queremos inicializar con el menor valor posible porque nos interesa el maximo:
# min_numero = float('-inf')

# si queremos inicializar con el mayor valor posible porque nos interesa el minimo:
# max_numero = float('inf')