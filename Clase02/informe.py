# alumno: mariano boronat
# ejercicios pertenecientes a la clase 3

import csv
from pprint import pprint

# %%
# 3.1
def leer_camion_tuplas(archivo):
    """definí una función leer_camion(nombre_archivo) que abre un archivo
    con el contenido de un camión, lo lee y devuelve la información como una lista de tuplas."""
    camion = []
    with open(archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for i, row in enumerate(rows):
            try:        
                lote = (row[0], int(row[1]), float(row[2])) #construye la tupla
                camion.append(lote) #agrega la tupla a la lista 'camion'
                print(lote)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return camion #devuelve la lista con todas las tuplas

# %%
# 3.2
def leer_camion(archivo):
    """Tomá la función que escribiste en el ejercicio anterior
    y modificala para representar cada cajón del camión con un diccionario
    en vez de una tupla. En este diccionario usá los campos "nombre", "cajones"
    y "precio" para representar las diferentes columnas del archivo de entrada."""
    camion = []
    with open(archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for i, row in enumerate(rows):
            try:
                # se crean los diccionarios  
                lote = {
                    "producto":row[0],
                    "cajones":int(row[1]),
                    "precio":float(row[2])
                    }
                camion.append(lote) #se añaden a la lista 'camion'
                # print(lote)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return camion


# %%
# 3.3
def leer_precios(archivo):
    """Escribí una función leer_precios(nombre_archivo) que a partir de un
    conjunto de precios como éste arme un diccionario donde las claves 
    sean los nombres de frutas y verduras, y los valores sean los precios por cajón.
    ej: {
    "naranja":10,
    "manzana":12,
    "banana":8
    }
    """
    precios = {}
    with open(archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for i, row in enumerate(rows):
            # print(i, row)
            if len(row) > 0:
                precios[row[0].lower()] = float(row[1])
                # se agrega el nuevo item al diccionario precios

            else:
                print('Faltan datos en la línea', i, 'del archivo.')

    return precios 

# %%
# 3.4
def calculo_recaudacion_venta(camion, precios):
    """calcule lo que costó el camión, lo que se recaudó con la venta, y la diferencia."""
    lista_camion = leer_camion(camion)
    lista_precios = leer_precios(precios)
    
    ganancia_total = 0

    recaudacion = {}

    # itero la lista de diccionarios del camion
    for camion in lista_camion:
        producto_camion = camion["producto"].lower()
        cajones_camion = camion["cajones"]
        precio_camion = camion["precio"]

        # por cada iteracion, itero la lista de precios de venta 
        # si coinciden los nombres realiza el calculo de ganancia
        # por producto
        for producto in lista_precios:
            precio_venta = lista_precios[producto]

            if producto.lower() == producto_camion:
                calculo = (precio_venta-precio_camion)*cajones_camion
                ganancia_total += calculo

                recaudacion[producto] = {
                                        "precio-camion": round(precio_camion,1),
                                        "recaudacion": precio_venta,
                                        "diferencia": round(precio_venta-precio_camion,1)
                                        }
    print(f"la ganancia total es de: ${ganancia_total}")
    return recaudacion


archivo_camion = "../Data/camion.csv"
archivo_precios = "../Data/precios.csv"

# 3.1
# print(leer_camion_tuplas(archivo_camion))

# # 3.2
# print(leer_camion(archivo_camion))

# # 3.3
# print(leer_precios(archivo_precios))

# 3.4
pprint(calculo_recaudacion_venta(archivo_camion, archivo_precios))