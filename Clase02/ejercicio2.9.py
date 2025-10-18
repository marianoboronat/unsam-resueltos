# alumno: mariano boronat

import csv

# Usando este código como guía, creá un nuevo archivo informe.py.
# En este archivo, definí una función leer_camion(nombre_archivo)
#  que abre un archivo con el contenido de un camión, lo lee y 
#  devuelve la información como una lista de tuplas. 
#  Para hacerlo vas a tener que hacer algunas modificaciones 
#  menores al código de arriba.


def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            try:
                print(i,row)
                ncajones = int(row[1])
                precio = float(row[2])
                total += ncajones * precio
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return total

costo_camion("../Data/camion.csv")
