#ALUMNO: mariano boronat
import csv
import gzip


archivo_camion = '../Data/camion.csv'

# %%
# 2.2
def precios_cantidad():
    """Escribí un programa llamado costo_camion.py que abra el archivo, 
    lea las líneas, y calcule el precio pagado por los cajones cargados en el camión."""

    with open(archivo_camion, 'rt') as f:
        primera_fila = next(f) # esta variable, guarda la primera fila del archivo

        # aca, arranca a iterar todo el resto de las filas
        for line in f:
            #cada fila la convierte en una lista 
            fila_en_lista = line.split(",")
            fruta = fila_en_lista[0]
            cantidad = int(fila_en_lista[1])
            precio = float(fila_en_lista[2].split("\n")[0])
            print(f"fruta: {fruta}, costo total: {round(precio * cantidad, 2)}")
        f.close()


# %%
# 2.3
def precio_naranja():
    lista_precios = '../Data/precios.csv'
    with open(lista_precios, 'rt') as f:
        primera_fila = next(f) # esta variable, guarda la primera fila del archivo

        for line in f:
            try:
                fila_en_lista = line.split(",")
                fruta = fila_en_lista[0]
                precio = float(fila_en_lista[1].split("\n")[0])
                if fruta.lower() == "naranja":
                    print(f"el precio de {fruta} es de ${precio}")

            except Exception as e:
                # si algo sale mal que siga iterando
                continue
        f.close()

# %%
# 2.4
def leer_gzip():
    with gzip.open('../Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')

# %%
# 2.5
def saludar(nombre):
    'Saluda a alguien'
    print('Hola', nombre)

# %%
# 2.6
def costo_camion(nombre_archivo):
    """Esta función recibe un nombre de archivo como entrada,
    lee la información sobre los cajones que cargó el camión y 
    devuelve el costo de la carga de frutas como una variable de punto flotante"""

    with open(nombre_archivo, 'rt') as f:
        primera_fila = next(f) # esta variable, guarda la primera fila del archivo
        # aca, arranca a iterar todo el resto de las filas
        for line in f:
            #cada fila la convierte en una lista 
            fila_en_lista = line.split(",")
            fruta = fila_en_lista[0]
            cantidad = int(fila_en_lista[1])
            precio = float(fila_en_lista[2].split("\n")[0])
            print(f"fruta: {fruta}, costo total: {round(precio * cantidad, 2)}")
        f.close()

# %%
# 2.7
def buscar_precio(fruta):
    """escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv
    el precio de determinada fruta (o verdura) y lo imprima en pantalla.
    Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique."""
    f = open("../Data/precios.csv")
    rows = csv.reader(f)
    headers = next(rows)

    encontrado = False

    for row in rows:
        # print(row)
        # si el tamaño de la fila es mayor a 0
        if len(row) > 0:
            # si la el nombre de la fruta dada en minuscula
            # es igual a la fruta leida
            if fruta.lower() == row[0].lower():
                print("el precio de ",fruta, " es de $", row[1])
                encontrado = True
                break
    f.close()

    if encontrado == False:
        print(fruta, "no existe en el listado.")
        

# %%
# 2.8
def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad


# 2.2
# precios_cantidad()

# 2.3
# precio_naranja()

# 2.4
# leer_gzip()

# 2.5
# saludar("pepito")

# 2.6
# archivo = "../Data/camion.csv"
# costo_camion(archivo)

# 2.7
buscar_precio("frutilla")