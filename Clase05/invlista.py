# alumno: mariano boronat

#%%
# 5.5
def invertir_lista(lista):
    """devuelva otra que tenga los mismos elementos pero en el orden inverso."""
    lista_inv = []
    indice = 0
    for item in lista:
        indice -= 1
        lista_inv.append(lista[indice])
    return lista_inv
        


if __name__ == "__main__":
    lista = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
    uni_pub = ["UNSAM","UNLAM", "UNLP", "UNC","UBA"]

    print(invertir_lista(uni_pub))