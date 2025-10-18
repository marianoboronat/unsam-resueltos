import csv
import informe_funciones


def leer_archivo(file):
    """
    permite leer un archivo csv.
    devuelve un objeto para procesar datos del csv
    """
    f = open(file)
    filas = csv.reader(f)
    return filas

def costo_camion(file):
        
    filas = leer_archivo(file)
    encabezados = next(filas)
    costo_total = 0

    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += round(ncajones * precio, 2)
            # print(costo_total)
        # Esto atrapa errores en los int() y float() de arriba.
            # print(record)
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total

datos = costo_camion("../Data/missing.csv")
print(datos)

# %%
# 7.9
archivo = "../Data/camion.csv"
# print(costo_camion(archivo))
informe_funciones.leer_camion(archivo)