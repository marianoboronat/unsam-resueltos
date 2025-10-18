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



if __name__ == "__main__":
    print(parametros)
    if len(parametros) <2:
        rebotes(100)
    else:
        rebotes(int(parametros[1]))
