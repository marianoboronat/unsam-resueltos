# mariano boronat 
# PROGRAMACION 1 - recuperatorio
import csv
import json

# %%
# punto 1
def leer_archivo(file):
    """lee el archivo
    Devuelve una TUPLA con el siguiente orden:
    (encabezados, data)
    """
    data = []
    with open(file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        print(f"Header: {header}")

        # Iterate over the remaining rows
        for i, row in enumerate(csv_reader):
            data.append(row)
    cantidad_pasajeros = len(data)
    return header, data, cantidad_pasajeros 

# %%
# punto 2
def seleccion_columnas(file, select:list):
    """
    permite filtrar el dataset segun las columnas que se especifiquen,
    df: se debe pasar la lista de datos
    select: debe ser una lista cuyos valores sean el nombre de las columnas
    RETURN: devuelve el dataframe con las columnas seleccionadas.
    """
    data = leer_archivo(file)
    filas = data[1]
    encabezados = data[0]
    print(encabezados)
    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        # print(indices)
        encabezados = select #reemplazo la por la lista dada como parametro.
    else:
        indices = []

    registros = []
    for fila in filas:
        if not fila:    # Saltear filas vacías
            continue
        # Filtrar la fila si se especificaron columnas
        if indices:
            fila = [fila[index] for index in indices]

        # Armar el diccionario
        registro = dict(zip(encabezados, fila))
        registros.append(registro)

    return registros

# punto 3
# Contar cuántas personas sobrevivieron y cuántas no
# ( NO SIRVE :c )

def sobrevivientes(file):
    data = seleccion_columnas(file, ["Survived"])
    sobrevivientes = []
    no_sobrevivientes = []

    for fila in data:
        # print(fila)
        if fila["Survived"] == "0":
            sobrevivientes.append(fila)
        elif fila["Survived"] == "1":
            no_sobrevivientes.append(fila)
    
    resultado = {
        "sobrevivientes":len(sobrevivientes),
        "no-sobrevivientes": len(no_sobrevivientes)
        }
    return resultado
    
# punto 3, 4 y 5
def precio_promedio(file):
    """
    devuelve en un diccionario:
    la cantidad de personas que sobrevivieron y las que no.
    el precio promedio del pasaje que pagaron las personas que sobrevivieron y las que no
    """
    data = seleccion_columnas(file, ["Survived", "Fare", "Age"])
    lista_precios_sobrevivientes = []
    lista_precios_no_sobrevivientes = []

    lista_edad_sobrevivientes = []
    lista_edad_no_sobrevivientes = []

    # recorro cada fila
    for fila in data:
        # print(fila)
        # en caso de haber algun error en los datos
        try:
            if fila["Survived"] == "1":
                lista_precios_sobrevivientes.append(float(fila["Fare"]))
                lista_edad_sobrevivientes.append(float(fila["Age"]))
                
            elif fila["Survived"] == "0":
                lista_precios_no_sobrevivientes.append(float(fila["Fare"]))
                lista_edad_no_sobrevivientes.append(float(fila["Age"]))
        except Exception as e:
            print(e)
    # • calculo los promedios distinguiendo sobrevivientes
    precio_prom_sobreviviente = 0.0
    precio_prom_no_sobreviviente = 0.0

    # precio promedio sobrevivientes
    for prom in lista_precios_sobrevivientes:
        # print(prom)
        precio_prom_sobreviviente += prom

    # precio promedio no sobrevivientes
    for prom in lista_precios_no_sobrevivientes:
        precio_prom_no_sobreviviente += prom
    
    # • calculo las edades promedio
    edad_prom_sobreviviente = 0.0
    edad_prom_no_sobreviviente = 0.0

    # promedio edad de sobrevivientes
    for prom in lista_edad_sobrevivientes:
        edad_prom_sobreviviente += prom

    # promedio edad de no sobrevivientes
    for prom in lista_edad_no_sobrevivientes:
        edad_prom_no_sobreviviente += prom

    resultados = {
        "sobrevivientes":{
            "cantidad":len(lista_precios_sobrevivientes),
            "precio-prom":round(precio_prom_sobreviviente / len(lista_precios_sobrevivientes), 1),
            "edad-prom":round(edad_prom_sobreviviente / len(lista_edad_sobrevivientes), 1)
            },
        "no-sobrevivientes":{
            "cantidad":len(lista_precios_no_sobrevivientes),
            "precio-prom":round(precio_prom_no_sobreviviente / len(lista_precios_no_sobrevivientes), 1),
            "edad-prom":round(edad_prom_no_sobreviviente / len(lista_edad_no_sobrevivientes), 1)
            }
        }
    
    return resultados

# punto 6
def supervivencia_genero(file):
    """devuelve la cantidad de supervivientes y no supervivientes por genero"""
    data = seleccion_columnas(file, ["Survived", "Sex"])
    resultados = {}

    fem_sobrevivientes = 0
    masc_sobrevivientes = 0
    fem_no_sobrevivientes = 0
    masc_no_sobrevivientes = 0

    for i, fila in enumerate(data):
        # sobrevivientes
        if fila["Survived"] == "1":
            if fila['Sex'] == "female":
                fem_sobrevivientes += 1
            if fila['Sex'] == "male":
                masc_sobrevivientes += 1
        # no sobrevivientes
        if fila["Survived"] == "0":
            if fila['Sex'] == "female":
                fem_no_sobrevivientes += 1
            if fila['Sex'] == "male":
                masc_no_sobrevivientes += 1
                
        # print(fila)

    resultados = {
        "sobrevivientes":{
            "femenino":fem_sobrevivientes,
            "masculino":masc_sobrevivientes,
            },
        "no-sobrevivientes":{
            "femenino":fem_no_sobrevivientes,
            "masculino":masc_no_sobrevivientes,
            }
        }
    return resultados

if __name__ == "__main__":
    nombre_archivo = "Titanic-Dataset.csv"
    columnas = ["Pclass", "Sex", "Age", "Fare", "Survived"]
    data = leer_archivo(nombre_archivo) 

    # punto 1
    print(f"lectura del archivo: {data [1]}")    
    print(f"la cantidad de pasajeros es de: {data [2]}")

    # punto 2
    print(seleccion_columnas(nombre_archivo, columnas))

    # punto 3, 4 y 5 (unifique las tres respuestas en una)
    # ACLARACION: para el punto 5, la funcion ignora los datos que no
    # tengan edad registrada
    print(json.dumps(precio_promedio(nombre_archivo), indent = 2))

    # punto 6
    print(json.dumps(supervivencia_genero(nombre_archivo),indent = 2))