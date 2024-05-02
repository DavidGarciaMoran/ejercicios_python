num = 1
while(num / 10000000 <= 1):
    num = int(input("Introduce tu número dni"))
    if(num / 10000000 <= 1):
        print("Número no reconocido")
   

dictLetras = {
    0 : "T",
    1 : "R",
    2:"W",
    3:"A",
    4:"G",
    5:"M",
    6:"Y",
    7:"F",
    8:"P",
    9:"D",
    10:"X",
    11:"B",
    12:"N",
    13:"J",
    14:"Z",
    15:"S",
    16:"Q",
    17:"V",
    18:"H",
    19:"L",
    20:"C",
    21:"K",
    22:"E"

}

resto = num % 23
print("Tu letra es ",dictLetras[resto])