"""Sacar por pantalla tablas de multiplicar"""

def mostrarTablas():
    for i in range(1,11):
        for j in range(1, 11):
            print(i, "X", j, "=",i*j, end = "\t")
        print()

mostrarTablas()