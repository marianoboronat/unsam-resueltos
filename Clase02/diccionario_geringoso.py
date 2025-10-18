lista_palabras = [
    "naranja",
    "manzana",
    "palta"
]

def convertir_geringoso(palabra):
    #primero defino la funcion que convierte una palabra en geringoso
    # extraido del ejercicio de la clase anterior.

    vocales = "aeiou"
    palabra_final = ""

    for letra in palabra:
        palabra_final += letra

        if letra in vocales:
            palabra_final += f"p{letra}"
    
    print(palabra_final)
    # devuelve la palabra en geringoso
    return palabra_final

def diccionario_geringoso(lista):
    """Construí una función que, a partir de una lista de palabras,
    devuelva un diccionario geringoso. Las claves del diccionario deben ser
    las palabras de la lista y los valores deben ser sus traducciones al geringoso """

    diccionario = {}
    for palabra in lista_palabras:
        # en cada iteracion
        diccionario[palabra] = convertir_geringoso(palabra)
    print(diccionario)
    return diccionario

diccionario_geringoso(lista_palabras)
