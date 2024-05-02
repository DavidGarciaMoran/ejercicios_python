
def sumL(l):
    suma = 0
    for num in l: suma += num
    return suma
    

def mulL(l):
    mulL = 1
    for num in l: mulL *= num
    return mulL
    

print(sumL([2,3,4]))
print(mulL([2,4,3]))