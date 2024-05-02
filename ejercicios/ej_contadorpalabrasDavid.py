"""
Crear una función que nos devuelva el número de apariciones de una
palabra concreta en una cadena.

p. ej = "Esta cadena tiene encadenadas otras cadenas con más cadenas"

"""
def contarPalabras(cadena, palabra):
    cantidad_palabras = 0
    copia_palabra = ""
    ##Para que siempre compruebe la ultima palabra
    cadena += " "

    for i in cadena:
        if i != (" " or "."):
            copia_palabra+= i
            ##print(copia_palabra)
        else:
            if copia_palabra == palabra:
                cantidad_palabras+=1
            copia_palabra = ""


    return cantidad_palabras


cadena_ej = "Esta cadena tiene encadenadas otras cadenas con más cadenas"
palabra = input("Dime una palabra ")
num = contarPalabras(cadena_ej, palabra)
print("Se repite", num, "veces")




