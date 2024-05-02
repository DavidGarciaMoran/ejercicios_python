a = range(1,10)
print(type(a))


def descuento(precio, puntos):
    if puntos < 100:
        precio = precio - precio * 10 / 100
    elif puntos > 100 and puntos < 150:
        precio = precio - precio * 12 / 100
    elif puntos == 150:
        precio = precio - precio * 15 / 100
    else:
        precio = precio - precio * 20 / 100
    return precio


print(descuento(500, 80))
print(descuento(500, 120))
print(descuento(500, 150))
print(descuento(500, 180))
print()
def esMayor(edad):
    return edad >= 18


print("Ejercicio tarifas")
trabajo = {"trabaja": True, "notrabaja":False}

def tarifas(tarifa, adulto, situacion):
    if not adulto and trabajo[situacion]:
        tarifa = tarifa - tarifa * 5 / 100
    elif adulto and not trabajo[situacion]:
         tarifa = tarifa - tarifa * 15 / 100
    elif not adulto and not trabajo[situacion]:
        tarifa = tarifa - tarifa * 50 / 100
    else:
        pass
        
    return tarifa

print(tarifas(1000,esMayor(18), "trabaja"))
print(tarifas(1000,esMayor(17), "trabaja"))
print(tarifas(1000,esMayor(18), "notrabaja"))
print(tarifas(1000,esMayor(17), "notrabaja"))

print()
print("Listas")




numeros = []
count = 10
while count > 0:
    count-= 1
    a =numeros.append(int(input("Ingresa el numero ")))

print("Suma:",sum(numeros))
print("Mayor:", max(numeros))
print("Menor:", min(numeros))
print("Promedio:",sum(numeros) / len(numeros))

