# mariano boronat
import sys

 
parametros = sys.argv  

def rebotes(altura):
    h = altura
    contador = 0

    while contador < 10:
        contador +=1 #incrementa el contador para poder detener el loop while

        h = round(h * (3/5),2)
        print(h)
     
# rebotes(int(parametros[1]) )

# ejecutar el siguiente comando en la consola:
# >>> py rebotes.py 100

# 3.10

def rebotes(altura = 100):
    h = altura
    contador = 0
    print("altura inicial: ", h)

    while contador <= 10:
        contador +=1 #incrementa el contador para poder detener el loop while

        h = round(h * (3/5),2)
        print(h)



# %%
# 3.10
print(parametros)
if len(parametros) <2:
    rebotes()
else:
    rebotes(int(parametros[1]))


# %%
# 3.11


