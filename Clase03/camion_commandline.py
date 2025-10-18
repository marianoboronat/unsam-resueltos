#ALUMNO: mariano boronat
# camion_commandline.py
import csv
import sys

archivo = "../Data/camion.csv"

def costo_camion(file):
    camion = []
    costo_total = 0
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
                costo_total += lote["precio"]*lote["cajones"]
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return costo_total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
    print(f"nombre archivo: {nombre_archivo}")
    print(costo_camion(nombre_archivo))
else:
    nombre_archivo = '../Data/camion.csv'

