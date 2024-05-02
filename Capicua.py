
num = input("Dime un número ")
lista = []

length = len(num)


lista = num[:: -1]

if(lista == num):
    print("Es capicua")
else:
    print("No es capicua")

print(lista)