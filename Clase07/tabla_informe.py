import csv
archivo_camion = "../Data/camion.csv"
archivo_precio = "../Data/precios.csv"

fecha_camion = "../Data/fecha_camion.csv"

def leer_archivo(archivo):
    f = open(archivo)
    filas = csv.reader(f)
    # encabezados = next(filas)
    lista = []
    for fila in filas:
        lista.append(fila)
    return lista 


def leer_precios(file):
    
    f = open(file)
    filas = csv.reader(f)
    # encabezados = next(filas)
    lista = []
    for fila in filas:
        lista.append(fila)
    return lista 

def hacer_informe():
    # junta los de leer_camion() y leer_precios() en una lista de tuplas.
    camion = leer_archivo(archivo_camion)
    precios = leer_archivo(archivo_precio)
    # print(camion, precios)
    # iterar camion.
    lista_tuplas = [["nombre", "cajones","precio", "cambio"]]
    for dato in camion:
        print(dato)
        for precio in precios:
            # y compararlo con leer_precios()
            try:
                if dato[0].lower()== precio[0].lower():
                    # print(f"{dato[0].lower()}{precio[0].lower()}")
                    tupla = (dato[0], int(dato[1]), float(dato[2]), float(precio[1])-float(dato[2]))
                    lista_tuplas.append(tupla)
            except Exception as e:
                "no se encontraron coincidencias."
    return lista_tuplas

def tabla_informe():
    informe = hacer_informe()
    encabezado = informe.pop(0)
    # print(encabezado)
    print(f"{encabezado[0]:>10s}{encabezado[1]:>10s}{encabezado[2]:>10s}{encabezado[3]:>10s}" )
    print(f"{("-"*10)}  "*4)
    for nombre, cajones, precio, cambio in informe:
        # print('%10s %10d %10.2f %10.2f' % dato)
        precio=f"${precio}"
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')


# print(hacer_informe())
tabla_informe()