"""Grupo David y Natalia"""
from random import choice
from random import randint
def getInput():
    selection = ""
    while selection != "pi" and selection != "p" and selection != "t":
        selection = input("Escribe Piedra(pi), papel(p) o tijeras(t)")
        if selection != "pi" and selection != "p" and selection != "t":
            print("Esribelo bien")
    return selection

def getRandomNumber(min, max):
    return randint(min,max)

def gameLogic(choice, bot, points, points_bot):
    if choice == bot:
        print("Empate")
        return points, points_bot
    elif choice == "p" and bot == "pi":
        print("Papel gana a piedra")
        return points+1, points_bot
    elif choice == "pi" and bot == "t":
        print("Piedra gana a tijera")
        return points+1, points_bot
    elif choice == "t" and bot == "p":
        print("Tijera gana a papel")
        return points+1, points_bot
    else:
        if bot == "pi":
             print("Bot gana, Piedra gana a tijera")
             return points, points_bot+1
        elif bot == "p":
            print("Bot gana, Papel gana a piedra")
            return points, points_bot+1
        else:
            print("Bot gana, Tijera gana a papel")
            return points, points_bot+1
    
    

def finalJuego(points_player, points_bot):
    if points_bot == 2:
        print("¡¡¡Ganó bot!!!")
        return True
    elif points_player == 2:
        print("¡¡¡Ganaste!!!")
        return True
    else:
        return False

def winner(points_player, points_bot):
    if points_bot > points_player:
        return False
    else:
        return True


    
def volverAJugar():
    print("Quieres volver a jugar? s/n")
    if(input() == "s"):
        return True
    else: return False

    

opciones = ["pi", "p", "t"]
opciones_string = ["Piedra", "Papel", "Tijera"]
winCount = 0
bot_winCount = 0
while True:
    points = 0
    points_bot = 0
    while finalJuego(points, points_bot) != True:
        rand = getRandomNumber(0,2)
        bot = opciones[rand]
        choice = getInput()
        
        print("Bot juega", opciones_string[rand])
        points, points_bot = gameLogic(choice, bot, points, points_bot)
        print("Jugador: ", points, "Bot: ", points_bot)
    
    if winner(points, points_bot):
        winCount+=1
    else:
        bot_winCount+=1
        

    print("Paridas ganadas por Jugador: ", winCount, "Partidas ganadas por bot ", bot_winCount)
    #termina el juego si no quiere volver a jugar
    if volverAJugar() == False:
        break


    
