import sys

def maxim(n1, n2):
    if n1 > n2: return n1
    else: return n2
    pass

def maxim_t(n1, n2, n3):
    max = 0
    if n1 > n2 and n1 > n3:
        max = n1
    elif n2 > n3:
        max = n2
    else:
        max = n3
    return max


def llen(list):
    
    size = list.__sizeof__()
    #40 es el tamaño de una lista
    size = size - 40
    
    return size // 8
    
       

print(maxim(89070700,13255))
print(maxim_t(0,3,2425))
l = [1,2,3,"wegwgw"]
print(llen(list(l)))

