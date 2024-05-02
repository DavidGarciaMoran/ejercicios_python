
def duplicado(l):
    #Lista no duplicados
    lnd = []

    index = 0
    indexReps = 0
    lnd.append(l[0])
    indexReps += 1
    for i in l:
        print(index)
        print(indexReps)
            
        #si el elemento que hay en lnd es distinto del actual
        if(lnd[index - indexReps] != l[index]):
            lnd.append(i)
            
        else:
            indexReps += 1
            
        index += 1
    return lnd


    
    
        
        
def encontrar_duplicados(lista):
    numeros_sin_duplicados = []
    vistos = {}  # Usaremos un diccionario para rastrear los elementos vistos
    tam = len(lista)
    runs = 0
    for i , j in zip(lista, reversed(lista)):
        vistos[i] = True
        vistos[j] = True
        runs+=1
        if(tam % 2 == 0):
            if runs >= tam//2:
                break
        else:
            if runs >= tam//2:
                vistos[lista[runs]] = ""
                break

    return vistos

# Ejemplo de uso
mi_lista = [1,4,3,6,6,6]
numeros_sin_duplicados = encontrar_duplicados(mi_lista)
nsd = list(numeros_sin_duplicados.keys()).copy()
nsd.sort()
print("Lista de números sin duplicados:", nsd)

#print(duplicadosx2([1,2,2,2,2,4,5,5], 0))
        
      