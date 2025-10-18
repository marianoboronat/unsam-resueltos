# alumno: mariano boronat
import random
import numpy as np


# %%
# 6.13
def crear_album(figus_total):
    """álbum (vector) vacío con figus_total espacios para pegar figuritas."""
    return np.array([0 for espacio in range(figus_total)])

# %%
# 6.14
def album_incompleto(A):
    """recibe un vector y devuelve True si el álbum A no está completo y False si está completo."""
    es_todo_uno = (A >= 1).all()
    if es_todo_uno == False:
        return True
    else:
        return False

# %%
# 6.15
def comprar_figu(figus_total):
    """reciba el número total de figuritas que tiene el álbum
    (dado por el parámetro figus_total) y devuelva un número entero
    aleatorio que representa la figurita que nos tocó."""

    figu_random = random.randint(0,len(figus_total)-1)
    return figu_random

# %%
# 6.16
def cuantas_figus(figus_total):
    """ dado el tamaño del álbum (figus_total) y usando las funciones
    anteriores, genere un álbum nuevo, simule su llenado, y devuelva
    la cantidad de figuritas que se debieron comprar para completarlo"""
    
    # puede crear de forma aleatoria un album de entre 10 y 25 fichus
    nuevo_album = crear_album(random.randint(10,25)) 

    figuritas_compradas = 0

    # mientras el album no este completo
    while album_incompleto(nuevo_album)==True:
        # compro figurita
        figurita = comprar_figu(nuevo_album)
        figuritas_compradas +=1
        nuevo_album[figurita] += 1

    # devuelve el album lleno
    return figuritas_compradas

# %%
# 6.17
def repeticiones(n_repeticiones ):
    """genere un álbum nuevo, simule su llenado, y devuelva la
      cantidad de figuritas que se debieron comprar para completarlo."""
    lista_cantidad_figuritas_compradas = [cuantas_figus(6) for x in range(n_repeticiones)]
    promedio = round(np.mean(lista_cantidad_figuritas_compradas),1)

    return promedio

# %%
# 6.18
def experimento_figus(n_repeticiones, figus_total):
    """simule el llenado de n_repeticiones álbums de figus_total figuritas
    y devuelva el número estimado de figuritas que hay que comprar, 
    en promedio, para completar el álbum."""
    lista_cantidad_figuritas_compradas = [cuantas_figus(figus_total) for x in range(n_repeticiones)]
    promedio = round(np.mean(lista_cantidad_figuritas_compradas),1)
    return promedio



if __name__ == "__main__":
    album = crear_album(8)
    # print(album)
    # 6.14
    print(album_incompleto(album))
    # 6.15
    print(comprar_figu(album))
    # 6.16
    print(cuantas_figus(album))
    # 6.17
    print(f"promedio figuritas compradas: {repeticiones(1000)}")

    # 6.18
    print(experimento_figus(100, 670))