print("Palabra a numeros")

'''
letters = map(chr, range(97, 123))

dicLetras = dict()
for index, item in enumerate (list(letters), 1):
    dicLetras[item] = index
palabra = input("Escribe palabra ")

palabra = palabra.lower()

for i in palabra:
    if i in dicLetras :
        print(dicLetras[i], end = "")
'''

palabra = input("Escribe palabra ")
palabra = palabra.lower()
for i in palabra:
    asc = ord(i)
    if(asc in range(97,123)):
        value = asc - 96
        print (value)