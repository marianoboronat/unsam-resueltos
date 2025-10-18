import csv
from pprint import pprint


archivo_1 = "../Data/camion.csv"
archivo_2 = "../Data/precios.csv"

def leer_precios(file):
    precios = {}
    with open(file, encoding='utf-8') as csvfile:
        rows= csv.reader(csvfile, delimiter=',')
        headers = next(rows)
        for row in rows:
            # t.sleep(0.2)
            try:
                precios[row[0]] = float(row[1])
            except:
                print('Faltan datos en la línea','del archivo.')
    return precios


def leer_camion(file):
    camion = []
    with open(file, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for i, row in enumerate(rows):
            try:        
                lote = {"producto":row[0],
                        "cajones":int(row[1]),
                        "precio":float(row[2])
                        }
                camion.append(lote)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return camion

def calculo_recaudacion_venta():
    """calculo recaudacion de la venta"""
    lista_camion = leer_camion(archivo_1)
    lista_precios = leer_precios(archivo_2)
    print("lsitade precios", lista_precios)
    ganancia_total = 0

    # itero la lista de camion
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
                print(f"producto: {producto}, ganancia: {calculo}")
    print(f"la ganancia total es de: ${ganancia_total}")




calculo_recaudacion_venta()