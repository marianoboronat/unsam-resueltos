# mariano boronat

vocales = "aeiou" # guardo en una variable las vocales.

palabra = "Geringoso"
palabra_final = ""


# itero la palabra a convertir, osea, recorro cada letra
for letra in palabra:
    
    # cada letra reccorida, se lo agrega a la variable 'palabra_final'
    palabra_final += letra

    if letra in vocales:
        # si la letra recorrida es una vocal, con una p adelante de ella se le agrega
        # a la variable'palabra_final'.
        palabra_final += f"p{letra}"


print(palabra_final)


