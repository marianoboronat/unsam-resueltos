#alumno: mariano boronat

#%%
# 5.3
def buscar_u_elemento(lista, elemento):
    """devuelva la posición de la última aparición de ese elemento en la lista"""
    # por defecto asumimos que no se encuentra
    indice = -1
    for i, item in enumerate(lista):
        if item ==elemento:
            indice = i
    return indice


def buscar_n_elemento(lista, elemento):
    """devuelva la cantidad de veces que aparece el elemento en la lista."""
    contador = 0
    
    for item in lista:
        if item == elemento:
            contador += 1
    return contador



#%%
# 5.4
def maximo(lista):
    '''Devuelve el máximo de una lista'''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo con el primer item
    
    for e in lista: 
        # la comparacion lo realizara a partir del primer item
        if e > m:
            m = e
    return m

def minimo(lista):
    """devuelve el minimo de una lista"""
    m = lista[0]

    for e in lista:
        if e < m:
            m = e
    return m


if __name__ == "__main__":
    lista = [-5,-10,-10.2,-10.25,-5]
    
    # 5.3
    print(buscar_u_elemento(lista, 2))
    print(buscar_n_elemento(lista, 5))

    # 5.4
    # print(minimo(lista))
