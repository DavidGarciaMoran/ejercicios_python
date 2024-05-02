"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
informando de ello.
Fruta Precio
Plátano 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70
"""

dicFrutas = {"Manzana": 0.8, "Platano": 1.35, "Pera": 0.85, "Naranja":0.7}
fruitList = ["Manzana", "Platano", "Pera", "Naranja"]

def pedirFruta():
    result = 0
    
    pedido = input("Que fruta quieres (0: Manzana, 1: Platano, 2: Pera, 3: Naranja) ")
    try:
        pedido = int(pedido) 
        if pedido >=0 and pedido < len(dicFrutas) :
            try:
                kilos = float(input("Cuantos kilos "))
            except:
                kilos = 0    
            #print(f"Has pedido {kilos} kilos de {fruitList[pedido]}, son {kilos * dicFrutas[fruitList[pedido]]}")
            #return list(dicFrutas.items())[pedido]
            result = (fruitList[pedido], kilos * dicFrutas[fruitList[pedido]]) 
        else:
            print("No tenemos esa fruta")
            result = None
    except:
        if(pedido == "nada"):
            result = "nada"
        else:
            result = None


    return result
    

cesta = {}
producto = ""

print("Añade frutas al carro")
while producto != "nada":
    producto = pedirFruta()
    if(producto == "nada"):
        print("Gracias por tu compra")  
    elif(producto == None):
        print("Pide otro producto")
    elif producto[0] in cesta:
        cesta[producto[0]] = (cesta[producto[0]][0] + 1, producto[1] + cesta[producto[0]][1])
    else:
        cesta[producto[0]] = (1, producto[1])
    
total = 0
for item in cesta.items():
    total += item[1][1]
    print(str(item[1][0]) + " de " + str(item[0]))


print("Precio total " + str(total)) 



