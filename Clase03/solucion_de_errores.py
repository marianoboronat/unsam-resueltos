# alumno: mariano boronat
#Ejercicio 3.1. Función tiene_a()

## CODIGO ORIGINAL

# def tiene_a(expresion):
#     "funcion original"
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         else:
#             return False
#         i += 1
# 
# print(tiene_a('UNSAM 2020'))
# print(tiene_a('abracadabra'))
# print(tiene_a('La novela 1984 de George Orwell'))

# EXPLICACION:
# el error que tiene es de tipo semantico, ya que el codigo
# en si funciona, pero no devuelve un resultado correcto
# cada vez que recorre una letra del string que se le pasa como parametro, 
# la funcion cambia de estado a verdadero o falso. 
# lo que provoca que si el string termina con un caracter distinto de "a", ¡LA FUNCION DEVUELVE FALSE!.
# para solucionar hice que la funcion cambie la variable 'letra_a' solo cuando es True.
# y dado que python es 'case sensitive',convierto todas las 'a' a minusculas para que no haya diferencias...


def tiene_a(expresion):
    """funcion corregida"""
    n = len(expresion)
    i = 0
    letra_a = False
    while i < n:
        if expresion[i].lower() == 'a':
            letra_a =True
        i += 1
    return letra_a


# print(tiene_a('UNSAM 2020'))
# print(tiene_a('abracadabra'))
# print(tiene_a('La novela 1984 de George Orwell'))

# %%
# Ejercicio 3.2.

# los errores son principalmente de tipo sintactico,
# pero tambien semantico ya que hay varias lineas que estan mal ubicadas.
# por empezar le falta los : a la definicion de la funcion,
# el loop while y el condicional if.
# ademas le falto el operador de comparacion '==' a la condicion 'if'
# y al igual que el ejercicio anterio le agregue una variable de tipo boolean
# para que almacene la informacion y la devuelva cuando el loop while finalice.

def tiene_a(expresion): # faltan los dos puntos
    n = len(expresion)
    i = 0
    letra_a=False
    while i<n : #faltan los dos puntos
        if expresion[i].lower() == 'a':#faltan los dos puntos y el signo de comparacion
            letra_a = True
        i += 1
    return letra_a
    # return Falso # Ademas falso.


#%%
#Ejercicio 3.3. Función tiene_uno()

# FUNCION ORIGINAL
# def tiene_uno(expresion):
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#         i += 1
#     return tiene

# la funcion emite un error en tiempo de ejecucion dado que al pasarle un 
# valor de tipo entero como parametro. 
# esto es porque la funcion  'len()' solo devuelve el tamanio de un valor que no sea numerico.
# Para solucionarlo simplemente converti el parametro 'expresion' a str al principio de la funcion. 

def tiene_uno(expresion):
    expresion = str(expresion) #convierto el valor que se ingrese a string
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

# print(tiene_uno(1995))
# print(tiene_uno("2025"))
# print(tiene_uno(98.1))







