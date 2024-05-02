def superposicion(l1,l2) -> bool:
    flag = False
    for i in l1:
        for j in l2:
            print(i, j)
            if(j == i):
                flag = True
    
    return flag


print(superposicion([1,2,3,4,4], [6,7,8,9,5]))
    
