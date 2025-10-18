import numpy as np
import matplotlib.pyplot as plt

# ejercicio 9.1
def ploteo():
    fig = plt.figure()
    plt.subplot(2, 1, 1) # define la figura de arriba
    plt.plot([0,1,2],[0,1,0]) # dibuja la curva
    plt.xticks([]), plt.yticks([]) # saca las marcas

    plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
    plt.plot([0,1],[0,1])
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
    plt.plot([0,1],[1,0])
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
    plt.plot([0,1],[1,1])
    plt.xticks([]), plt.yticks([])

    plt.show()


def randomwalk():
    caminatas = 10
    N = 10000
    

    lista_caminatas = []

    for x in range(caminatas):
        color = np.random.rand(3)    
        pasos = np.random.randint (-1,2,N)  #genera un array  
        caminata = pasos.cumsum() # recorre cada valor para proyectar la linea
        lista_caminatas.append(caminata)
        plt.plot(caminata, label='Pasos aleatorios', color=color, linewidth=0.5/2)
    
    # ploteo
    plt.show()
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')




if "__main__" == __name__:
    # 9.1
    # ploteo()
    
    # 9.2
    randomwalk()
