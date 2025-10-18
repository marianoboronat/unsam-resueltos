# alumno: boronat, mariano
# con los ejercicios 4.13 al  4.19.
import csv
from collections import Counter
import json


archivo = "../Data/arbolado-en-espacios-verdes.csv"

def leer_archivo(file):
    lista = []
    headers = []
    with open(file, encoding='utf-8') as csvfile:
        rows= csv.reader(csvfile, delimiter=',')
        headers = next(rows)
        for row in rows:
            lista.append(row)
    return lista, headers

# %%
# 4.13
def leer_parque(nombre_archivo, parque=None):
    # abrir el archivo
    # devolver una lista de diccionarios 
    # con la informacion del parque especificado.    
    # por cada arbol debe ser un diccionario
    datos = leer_archivo(nombre_archivo)
    cabecera = datos[1]
    # print(cabecera)
    lista_data = []
    for dato in datos[0]:
        diccionario = dict(zip(cabecera, dato))

        # si se especifica un parque
        if parque != None:
            if diccionario["espacio_ve"].lower() == parque.lower(): 
                lista_data.append(diccionario)
            

        # si no se especifica un parque
        else:
            lista_data.append(diccionario)
    
    # print(lista_data )
    # print(f"la lista tiene {len(lista_data)} datos")## la lista tiene 690 datos
    return lista_data

# %%
# 4.14
def especies(lista_arboles):
    lista_especies = []

    for dato in lista_arboles:
        especie = dato["nombre_com"].lower()
        lista_especies.append(especie)
    set_datos = set(lista_especies) 
    # print(set_datos,f"La lista tiene: {len(set_datos)} datos")
    return set_datos


# %%
#4.15
def contar_ejemplares(lista_arboles):
    # print(json.dumps(lista_parque,indent=2))
    lista_cantidad = {}
    lista_cantidad["parque"] =  lista_arboles[0]["espacio_ve"]

    lista_especies = []
    for dato in lista_arboles:
        lista_especies.append(dato["nombre_com"])
    
    cantidad_por_especie = Counter(lista_especies).most_common()

    # almacena las primeras 5 especies mas recurrentes en un "espacio verde"
    for i, cantidad in enumerate(cantidad_por_especie):
        if i < 5:
            lista_cantidad[cantidad[0]]=cantidad[1]
        else:
            break
    
    return lista_cantidad


# %%
#4.16
def obtener_alturas(lista_arboles, especie):
    """calcula el promedio y altura máxima de la especie determinada"""
    
    diccionario = {
        "parque":lista_arboles[0]["espacio_ve"],
        "especie":especie,
    }

    # aca se almacena todas las alturas
    lista_alturas = [] 

    # itera la lista de dicc de los arboles pertenecientes a un parque
    for arboles in lista_arboles: 
        if arboles["nombre_com"].lower() == especie.lower():
            try:
                altura = float(arboles["altura_tot"])
                lista_alturas.append(altura)
            except:
                print("no se puede convertir a numero este valor")

    diccionario["alt_promedio"] = round(sum(lista_alturas) / len(lista_alturas),1)
    diccionario["alt_max"] = max(lista_alturas)

    print(diccionario)
    return diccionario

# %%
#4.17
def obtener_inclinaciones(lista_arboles, especie):
    """devuelve una lista de las inclinaciones
    de una especie """
    
    diccionario = {
        "parque":lista_arboles[0]["espacio_ve"],
        "especie":especie,
    }

    # aca se almacena todas las inclinaciones
    lista_inclinaciones = [] 

    # itera la lista de dicc de los arboles pertenecientes a un parque
    for arboles in lista_arboles: 
        if arboles["nombre_com"].lower() == especie.lower():
            try:
                altura = float(arboles["inclinacio"])
                lista_inclinaciones.append(altura)
            except:
                print("no se puede convertir a numero este valor")
                continue
            
    return lista_inclinaciones

# %%
#4.18
def especimen_mas_inclinado(lista_arboles):
    # print(lista_arboles)
    set_especies = list(especies(lista_arboles)) # lo convierto a lista para mas comodidad.
    set_especies.sort()

    #se almacena 'especie': 'inclinacion'
    dict_inclinaciones = {}
    
    #se itera la lista de especies que tiene el parque
    for especie in set_especies:
        # print(especie)
        inclinacion_maxima = max(obtener_inclinaciones(lista_arboles,especie ))
        dict_inclinaciones[especie] = inclinacion_maxima
    
    especie_max = max(dict_inclinaciones, key = dict_inclinaciones.get)
    return {especie_max:dict_inclinaciones[especie_max]}


# %%
# 4.19
def especie_promedio_mas_inclinada(lista_arboles):
    """devuelva la especie que en promedio tiene la mayor inclinación y el promedio calculado."""
    set_especies = list(especies(lista_arboles)) # lo convierto a lista para mas comodidad.
    set_especies.sort()

    # una lista de diccionarios, donde se almacena las especies y sus promedios
    diccionario_prom = {}

    # itera cada especie del parque.
    for especie in set_especies:
        # print(especie)
        # se obtiene la lista de inclinaciones de la especie
        lista_inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        promedio_inclinaciones = round(sum(lista_inclinaciones)/len(lista_inclinaciones),1)
        #se agrega al diccionario
        diccionario_prom[f"{especie}"] = promedio_inclinaciones

    promedio_max = max(diccionario_prom, key = diccionario_prom.get)
    return {promedio_max:diccionario_prom[promedio_max]}


if __name__ == "__main__":
    # ir descomentando para probar
    
    ## 4.13 estas variables devuelven listas, para usar en las funciones de los
    # siguientes ejercicios
    lista_arboles_gral_paz = leer_parque(archivo,"general paz")
    lista_arboles_los_andes = leer_parque(archivo,"ANDES, LOS")
    lista_arboles_parque_centenario = leer_parque(archivo,"CENTENARIO")
    ## 4.14
    # print(especies(lista_arboles_parque_centenario))

    ## 4.15
    # print(contar_ejemplares(lista_arboles_gral_paz))

    ## 4.16
    # obtener_alturas(lista_arboles_gral_paz, "Tipa blanca")

    ## 4.17    
    # obtener_inclinaciones(lista_arboles_parque_centenario, "Falso Guayabo (Guayaba del Brasil)")

    ## 4.18
    # print(especimen_mas_inclinado(lista_arboles_gral_paz))

    ## 4.19
    print(especie_promedio_mas_inclinada(lista_arboles_parque_centenario))
