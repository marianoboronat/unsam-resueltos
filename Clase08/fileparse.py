# alumno: boronat mariano

import os
import sys
import csv


def change_dir():
    """cambia la ruta de ejecucion, a la del archivo"""
    # este script lo saque de chatGPT
    # Obtener la ruta del script actual
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Cambiar el directorio actual de trabajo a la carpeta del script
    os.chdir(script_dir)

    # Ahora puedes ejecutar comandos como si estuvieras en esa carpeta
    print(f"Directorio cambiado a: {os.getcwd()}")


# %%

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors  = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        registros = []

        # ejercicio 8.1: generando un error
        if select != None and has_headers == False:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
        else:
            # Lee los encabezados del archivo
            # si el archivo tiene encabezados
            if has_headers:
                encabezados = next(filas)

                # Si se indicó un selector de columnas,
                #    buscar los índices de las columnas especificadas.
                # Y en ese caso achicar el conjunto de encabezados para diccionarios

                if select:
                    indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                    print(indices)
                    encabezados = select
                else:
                    #si no hay filtros seleccionados
                    indices = []

                for i,fila in enumerate(filas):
                    # ejercicio 8.2: capturando errores
                    try:
                        if not fila:    # Saltear filas vacías
                            continue
                        # Filtrar la fila si se especificaron columnas
                        if indices:

                            fila = [fila[index] for index in indices]

                            # si asignamos una fila de tipo de datos, convertimos los valores
                        if types:
                            fila = [tipo_dato(val) for tipo_dato, val in zip(types, fila) ]
                            # print(fila)
                        # Armar el diccionario
                        registro = dict(zip(encabezados, fila))
                        registros.append(registro)
                    except Exception as e:
                        # ejercicio 8.3: silenciando errores
                        if silence_errors == True:
                            print(f"Fila {i}: No pude convertir {fila}")
                            print(f"Fila {i}: Motivo: {e}")
                        else:
                            continue

            else:
                for fila in filas:
                    if len(fila)==0 or not fila:    # Saltear filas vacías
                        continue
                    else:
                        registros.append(tuple(fila))

        return registros



if __name__ == "__main__":
    # archivos
    archivo = "../Data/camion.csv"
    archivo_error = "../Data/missing.csv"

    lista_columnas = ["precio","cajones"]
    tipos_de_datos= [str,float ]
    # 8.1
    # print("ejercicio 8.1:", parse_csv(archivo, select=None, has_headers=False ))

    # 8.2
    print("ejercicio 8.2:",parse_csv(archivo_error, types = [str, int, float],silence_errors = True))
    
    # 8.3
    # print("ejercicio 8.3:",parse_csv(archivo_error, types = [str, int, float], silence_errors = False))