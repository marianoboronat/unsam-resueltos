# mariano boronat

import time as t

# 7.10
def busqueda_lineal_lordenada(lista, e):
    '''
    la función para cuando encuentre un elemento mayor a e
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z > e:   # si encontramos a e
            print(z, e)
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos


def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos





if __name__ == "__main__":
    lista_ordenada = [x for x in range(10)]

    # 7.10
    print(busqueda_lineal_lordenada(lista_ordenada,7))

    # 7.11
    # print(donde_insertar(lista_ordenada, 5))