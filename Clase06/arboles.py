# alumno: boronat mariano
import csv
import json
import os
import numpy as np
import matplotlib.pyplot as plt


def leer_archivo(file):
    lista = []
    headers = []
    with open(file, encoding='utf-8') as csvfile:
        rows= csv.reader(csvfile, delimiter=',')
        headers = next(rows)
        for row in rows:
            lista.append(row)
    return lista, headers

#%%
# 5.15
def leer_arboles(nombre_archivo):
    """devuelva una lista de diccionarios con la información de todos 
    los árboles en el archivo."""
    arboleda = []
    datos = leer_archivo(nombre_archivo)
    cabecera = datos[1]
    # print(cabecera)
    for dato in datos[0]:
        diccionario = dict(zip(cabecera, dato))
        arboleda.append(diccionario)
    return arboleda


#%%
# 5.16
def lista_altura(lista_arboles, especie):
    # arma la lista de la altura de los árboles, segun la 
    # especie determinada...

    H = [float(data["altura_tot"]) for data in lista_arboles if data["nombre_com"].lower()==especie.lower()]
    return H

#%%
# 5.17
def altos_y_diámetros(lista_arboles, especie ):
    H = [(float(data["altura_tot"]),float(data["diametro"])) for data in lista_arboles if data["nombre_com"].lower()==especie.lower()]
    return H

# %%
# 5.18
def medidas_de_especies(especies,arboleda):
    """nueva lista que tenga pares (tuplas de longitud 2) conteniendo 
    no solo el alto sino también el diámetro de cada Jacarandá en la lista."""

    diccionario = { especie : altos_y_diámetros(arboleda, especie) for especie in especies }
    return diccionario

# %% 
# 6.10
def histograma_altos(especie):
    """generá un histograma con las alturas de los Jacarandás en el dataset."""
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = lista_altura(arboleda,especie)
    # print(altos)
    plt.hist(altos,bins=50)

    plt.xlabel("Altura de los ejemplares (metros)")       # Etiqueta del eje X
    plt.ylabel("cantidad de ejemplares")    # Etiqueta del eje Y
    plt.title(f"Cantidad de alturas de {especie}")  # Título del gráfico
    plt.show()

# %% 
# 6.11

def scatter_hd(especie):
    """ a partir de una lista de pares como la que generaste en 
    el Ejercicio 5.17 genere un scatterplot para visualizar la relación 
    entre altura y diámetro de los Jacarandás del dataset."""

    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    lista_altos_diam = altos_y_diámetros(arboleda,especie)
    
    altos = [h[0] for h in lista_altos_diam]
    diametros =  [d[1] for d in lista_altos_diam]

    # print(json.dumps(lista_altos_diam, indent=2))
    # print(altos,diametros)

    # diametro y altura
    plt.scatter(altos,diametros)

    plt.xlabel("Altura de los ejemplares (metros)")       # Etiqueta del eje X
    plt.ylabel("Diametro de los ejemplares")    # Etiqueta del eje Y
    plt.title(f"Cantidad de alturas de {especie}")  # Título del gráfico
    plt.show()
# %% 
# 6.12

def scatter_hd_multiples(especies:list):
    """hacé tres gráficos como en el ejercicio anterior, uno por cada especie."""
    
    archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(archivo)
    medidas = medidas_de_especies(especies, arboleda)

    for especie in medidas:
        print(medidas.items())
        lista_altos_diam = medidas[especie]
        altos = [h[0] for h in lista_altos_diam]
        diametros =  [d[1] for d in lista_altos_diam]
        
        plt.scatter(altos,diametros, alpha=0.3, )
        plt.legend(medidas.keys())

    plt.grid()
    plt.xlabel("Altura (metros)")       # Etiqueta del eje X
    plt.ylabel("Diametro (centímetros)")    # Etiqueta del eje Y
    plt.title(f"Diametros y alturas de ejemplares\nde árboles de diferentes especies.")  # Título del gráfico
    plt.show()

        # plt.scatter(altos,diametros)




if __name__ == "__main__":
    archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(archivo)
    especies = [ 'Brachichiton (Árbol botella, Brachichito)', "Álamo plateado"]
    # 6.10
    # scatter_hd(especies[0])

    # 6.12
    scatter_hd_multiples(especies)
    # cuanta mas 

