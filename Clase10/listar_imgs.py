# alumno: boronat, mariano
import os
import sys


# 10.5
def archivos_png(directorio):
    """un programa que dado un directorio, imprima en pantalla los nombres de 
    todos los archivos .png que se encuentren en algún subdirectorio del él"""
    raiz = os.getcwd()
    
    lista_imagenes= []

    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name.split(".")[-1]=="png": 
                lista_imagenes.append(name)

    return lista_imagenes



if __name__ =="__main__":
    lista_argumentos = sys.argv


    # 10.5
    if len(lista_argumentos) == 1:
        #ejecutar desde la carpeta de este archivo python
        print(archivos_png("../Data"))
    else:
        parametro = lista_argumentos[1]
        print(archivos_png(parametro))
        # print(parametro)

