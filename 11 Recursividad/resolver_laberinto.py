def resolver_laberinto(laberinto,x,y, camino):
    #Caso base: Si estamos fuera de los limites
    # o en un espacio bloqueado, detener.
    if (x < 0  or y < 0 or x >= len(laberinto) or y >= len(laberinto[0]) or laberinto[x][y] == 1):
        return False

    #Agregar la posicion actual al camino porque puedo avanzar
    camino.append((x,y))

    #Caso base: Si hemos llegado a la esquina inferior derecha, 
    #hemos encontrado el camino
    if (x == len(laberinto) - 1 and y == len(laberinto[0]) - 1):
        return True
    
    #Marcar el lugar actual como visitado par evitar ciclos.
    laberinto[x][y] = 1

    #Intentar moverse en cada una de las cuatro direcciones: 
    #Abajo, Derecha, Arriba, Izquierda
    if (resolver_laberinto(laberinto, x+1 , y, camino) or
        resolver_laberinto(laberinto, x, y+1, camino) or
        resolver_laberinto(laberinto, x-1, y, camino) or
        resolver_laberinto(laberinto, x, y-1, camino)):
        return True

    # Si ninguna direccion funcionó, hacker "backtracking":
    # Eliminar la posicion actual del camino y desmarcar la celda
    camino.pop()
    laberinto[x][y] = 0
    return False