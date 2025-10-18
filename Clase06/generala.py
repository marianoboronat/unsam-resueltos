import random
from pprint import pprint
from collections import Counter

# %%
# 6.1
def tirar():
    """ devuelva una lista con cinco dados generados aleatoriamente"""
    tirada = [random.randint(1,6) for x in range(5)] #list comprehention
    return tirada

def es_generala(tirada):
    numero = tirada[0]
    generala_servida = True 
    for dado in tirada:
        if dado != numero:
            generala_servida=False
    return generala_servida


# %%
# 6.2

def prob_generala(N):
    """a partir de un parámetro N y usando las funciones del Ejercicio 6.1
      realice una simulación con N repeticiones, para estimar la probabilidad
      de obtener una generala al finalizar una mano de tres tiradas. """

    N= 10000
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    return prob 

if __name__ =="__main__":
    

    prob_generala(10000)