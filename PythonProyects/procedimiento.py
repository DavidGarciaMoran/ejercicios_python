from ej10 import multiplicaCaracter
def procedimiento(l):
    for i in l:
        #print(multiplicaCaracter("*", i))
        l2 = [i * "*" for i in l]
    for i in l2:
        print(i)

    
procedimiento([5,7,2])