# Alumno: boronat Mariano
import random
import numpy as np
import os

# %%
#6.6

def medir_temp(n ):
    """simulá usando normalvariate() (con mu y sigma adecuados) n valores
    medidos por el termómetro. Escribí una función llamada medir_temp(n)
    que simule n mediciones y las devuelva en una lista."""

    nombre_archivo = "../Data/temperaturas.npy"
    

    mediciones = []
    temperatura = 37.5
    for intento in range(n):
        error_distribucion = random.normalvariate(0, 0.2) #media de 0, y un desvio de error
        medicion = temperatura + error_distribucion
        # print(error_distribucion, medicion)
        mediciones.append(medicion)
    
    np.save(nombre_archivo, mediciones)
    return np.array(mediciones)

def resumen_temp(n):
    """realice una simulación de n temperaturas (usando la
    función medir_temp(n)) y devuelva una tupla con el valor máximo,
     el mínimo, el promedio y la mediana (en ese orden) de estas n mediciones. """
    
    mediciones = medir_temp(n)

    valor_min = min(mediciones)
    valor_max = max(mediciones) 
    promedio = sum(mediciones) / n

    # para la mediana obtengo la cantidad que hay en la lista de mediciones y lo divido por 2
    #le puse round para que al indice se le asigne un entero
    mediana = mediciones[round(n/2)] 
    
    valores_mediciones = (valor_min,valor_max,promedio,mediana)        
    return valores_mediciones



if __name__ == "__main__":
    # print(resumen_temp(1000))

    # 6.8
    medir_temp(999)

    leer_datos = np.load('../Data/temperaturas.npy')
    print(leer_datos)