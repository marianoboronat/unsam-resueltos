import numpy as np
import matplotlib.pyplot as plt
import temperatura


# %%
# 6.9
def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')

    plt.hist(temperaturas,bins=50)
    plt.show()


if __name__ == "__main__":
    plotear_temperaturas()