# alumno: boronat mariano
import csv
import json

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
    print(diccionario)


if __name__ == "__main__":
    archivo = "../Data/arbolado-en-espacios-verdes.csv"
    lista_arboles = leer_arboles(archivo)
    lista_especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

    # 5.16
    lista_altura(lista_arboles,"Brachichiton (Árbol botella, Brachichito)")
    
    # 5.17
    print(altos_y_diámetros(lista_arboles,"jacarandá"))

    # 5.18
    medidas_de_especies(lista_especies,lista_arboles)

