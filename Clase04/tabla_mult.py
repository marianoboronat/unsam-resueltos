#alumno: mariano boronat

def cuentas():
    numeros = [x for x in range(0,10)]

    #solo para imprimir el encabezado
    encabezado = f"{"":<5}"
    for col in numeros:
        encabezado += f"{col:<5}"
    print(encabezado)

    #trazo de linea
    trazr_linea=  "-"*55
    print(trazr_linea)

    for columna in numeros:

        fila_formateada =""
        columna_string = f"{columna}:"
        fila_formateada +=f"{columna_string:<5}" 
        for valor in numeros:
            resultado = valor * columna
            fila_formateada += f"{resultado:<5}"
        print(fila_formateada)


cuentas()