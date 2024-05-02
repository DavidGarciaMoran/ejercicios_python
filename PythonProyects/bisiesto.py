
def bisiesto(año):
    año = int(año)
    flag = False
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                flag = True
        else:
            flag = True
    else:
        flag = False
    return flag


print(bisiesto(input("Es bisiesto?: ")))