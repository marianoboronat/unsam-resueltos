# alumno: mariano boronat

# 5.6
def propagar(lista_inicial):
    lista_propagada = lista_inicial.copy() 
    n = len(lista_propagada)
    cambiado = True 
    print(lista_inicial)
    
    while cambiado:
        cambiado = False
        for i in range(n):
            if lista_propagada[i] == 1:
                # propagar hacia la izquierda
                if i > 0 and lista_propagada[i - 1] == 0:
                    lista_propagada[i - 1] = 1
                    cambiado = True
                # propagar a la derecha
                if i < n - 1 and lista_propagada[i + 1] == 0:
                    lista_propagada[i + 1] = 1
                    cambiado = True
    return lista_propagada


if __name__ == "__main__":
    print(propagar([0,0,1,-1,0,0,0,-1,0,0,1]))
