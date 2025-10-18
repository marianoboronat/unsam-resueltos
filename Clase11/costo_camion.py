import csv
import lote

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
        try:
            instancia = lote.Lote(fila[0], float(fila[1]),float( fila[2]))
            costo_total += round(instancia.cajones * instancia.precio, 2)
            print(n_fila, costo_total)
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total


# %%
if __name__ == "__main__":
    archivo = "../Data/camion.csv"
    # datos = costo_camion("../Data/missing.csv")
    print(costo_camion(archivo))