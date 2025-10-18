# alumno: mariano boronat
import csv
import lote
import formato_tabla
import sys
import os

# %%
# 11.4
def leer_camion(nombre_archivo):
    """lea un archivo con el contenido de un camion y devuelva una lista de instancias
    de Lote como mostramos recién en el Ejercicio 11.3."""
    camiones = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)        
        for n_fila, fila in enumerate(filas, start = 1):
            try:
                instancia = lote.Lote(fila[0], fila[1],float(fila[2]))
                camiones.append(instancia)
            except ValueError:
                print('Faltan datos en la línea', n_fila, 'del archivo.')
    return camiones


def leer_precios(nombre_archivo):
    """devuelve un diccionario"""
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):            
            if row: #### en vez del try-except se puede usar un if
                precios[row[0]] = float(row[1])
    return precios

def hacer_informe(camion_file, precios_file):
    lista = []
    for lote in leer_camion(camion_file):
        precio_venta = leer_precios(precios_file)[lote.nombre]
        cambio = round(precio_venta - lote.precio, 1)

        t = (lote.nombre, int(lote.cajones), lote.precio, cambio)
        t = [str(x) for x in t]
        lista.append(t)

    return lista

# 11.5
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas con (nombre, cajones, precio, cambio) 
    '''

    formateador.encabezado(('Nombre','Cajones','Precio','Cambio'))
    for row in data_informe:
        formateador.fila(row)
    #         Nombre    Cajones     Precio     Cambio
    #  ---------- ---------- ---------- ----------
    #       Lima        100      $32.2       8.02
    #    Naranja         50      $91.1      15.18
    #      Caqui        150    $103.44       2.02

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(archivo_camion, archivo_precios)

    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt) # 11.7
    imprimir_informe(data_informe, formateador)


if __name__ == "__main__":
    archivo_camion = "../Data/camion.csv"
    archivo_precios = "../Data/precios.csv"

    # print(hacer_informe(archivo_camion, archivo_precios))
    
    # informes
    # 11.8
    # informe = informe_camion(archivo_camion, archivo_precios, fmt = "csv")

    """permite pasar los argumentos atraves de la terminal, o
    si no, ejecuta el programa de forma directa."""
    if len(sys.argv) == 4:
        nombre_archivo_camion = sys.argv[1]
        nombre_archivo_precios = sys.argv[2]
        formato = sys.argv[3]

        print(sys.argv)
        informe_camion(nombre_archivo_camion, nombre_archivo_precios, formato)

    else:
        informe_camion(archivo_camion, archivo_precios)