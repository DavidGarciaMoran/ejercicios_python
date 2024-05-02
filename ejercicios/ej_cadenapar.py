
##cad = input("Dame una cadena ")
##print(cad[1::2])


cadNum = input("Dame una cadena de numeros ")
i = 0
for num in cadNum:
    if int(num)%2 != 0:
        cadNum = cadNum[:i] + cadNum[i+1:] 
        i-=1
        print(cadNum)
    i+=1

print(cadNum)
