from math import sqrt as raiz

def funcion(x):
    try:
        formula = ( raiz(x+4) / ((raiz(x+3)) * (raiz(x-1))) )
        print("x: ", x ,"y: ",formula)
    except Exception as e:
        # print("tuvimos un error: ",e)
        print(type(e))


def iteracion():
    # numero de repeticiones
    numero = -10
    for x in range(0,20):
        numero = numero + 1
        funcion(numero)

iteracion()