from random import randint

def crearDiccionario(tam):
    dic = {num:False for num in range(0,tam)}
    return dic

def mostrarPalabraOculta():
    for i in range(0,len(palabra_oculta)):
        if(palabra_oculta[i] == False):
            print("_", end=" ")
        else:
            print(palabra_elegida[i], end= " ")
    

def finDePartida(result):   
    if result is True:
        response = input("Ganaste, escribe s si quieres volver a jugar ")
    else:
        response = input("Perdiste, escribe s si quieres volver a jugar ")
    if response == "s":
        return True
    else:
        return False

palabras = ["camaleon", "espantapajaros", "viñedo", "jirafa", "ram", "giroscopio", "amarillo", "engatusar", "triquiñuela", "albedrio"]
newGame = True
endGame = False

#Bucle principal del juego
while endGame != True:
    #Inicializo el juego si es una nueva partida
    if(newGame is True):
        ##Elije una palabra al azar
        palabra_elegida = palabras[randint(0, 9)]
        newGame = False
        num_fallos = 0
        ##Calcula el tamaño de la palabra
        tam_palabra = len(palabra_elegida)

        print("Si llegas a 10 fallos pierdes")
        palabra_oculta = {}
        palabra_oculta = crearDiccionario(tam_palabra)
    
    ##Muestra la palabra oculta con los huecos y letras descubiertas
    mostrarPalabraOculta()
    
    print(" Fallos:", num_fallos)

    ##Recoje una letra en el input
    letra = input("Escribe una letra: ")  
    #Si esa letra está en la palabra
    if letra in palabra_elegida:
        #Posición de la letra actual
        id_letra = 0
        for i in palabra_elegida:
            if i == letra:
                #Se desoculta la letra
                palabra_oculta[id_letra] = True
            id_letra += 1
    else:
        num_fallos += 1
    
    if(num_fallos >= 10):
        print("La palabra era", palabra_elegida)
        #False miuestra el mensaje de perder
        if finDePartida(False):
            newGame = True
        else:
            endGame = True
    else:
        flag = False
        for i in palabra_oculta.values():
            if i == True:
                flag = True
            else:
                flag = False
                break

        if flag:
            print(palabra_elegida)
            #True muestra el mensaje de ganar
            if finDePartida(True):
                newGame = True
            else:
                endGame = True
            
       
       

     




                

     


