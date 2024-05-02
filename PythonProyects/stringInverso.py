
def inversa(palabra):
    inversa = ""
    count = 0
    while palabra:
        inversa = palabra[:-count]
    
    print(inversa)

inversa("hola")