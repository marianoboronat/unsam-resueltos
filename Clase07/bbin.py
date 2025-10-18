# alumno: boronat, mariano
# 7.11
def donde_insertar(lista, x):
    """recibe una lista ordenada y un elemento y devuelva la 
    posición de ese elemento en la lista (si se encuentra en la lista)
    o la posición donde se podría insertar el elemento para que la lista
    permanezca ordenada (si no está en la lista)."""
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    # mientras izquierda sea menor que la derecha
    while izq < der:
        # print(f"izquierda: {izq}, derecha: {der}")
        medio = (izq + der) // 2
        # print(f"medio: {medio}")
        if lista[medio] < x:
            
            izq = medio + 1
            # print(f"izq: {izq}")
        else:
            der = medio            
            # print(f"der: {der}")
    return izq

# 7.12
def insertar(lista, x):
    """reciba una lista ordenada y un elemento. Si el elemento 
    se encuentra en la lista solamente debe devolver su posición;
     si no se encuentra en la lista, lo debe insertar en la posición 
     correcta para mantener el orden y devolver su posición (no 
     debe devolver la lista). Su funcionamiento debería ser así:"""
    lista = [1, 2, 3]
    insertar(lista, 2)


if __name__ == "__main__":
    lista_ordenada = [0,2,3,5,7,8,11]
    
    # 7.11
    print(donde_insertar(lista_ordenada, 6))

    # 7.12
