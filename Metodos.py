def LimitesMatriz(i, j, matriz):
    #Comprueba si la posicion existe en la matriz
    if(i>=0 and i<len(matriz)):
        if(j>=0 and j<len(matriz[i])):
            return True

    return False

def Busqueda(i, j, matriz):  
    if(LimitesMatriz(i,j,matriz) and matriz[i][j]==1):
        #Marca la posicion como leida
        matriz[i][j]=2 
        #Evalua las posiciones a su alrededor
        Busqueda(i - 1, j, matriz)
        Busqueda(i - 1, j + 1, matriz)
        Busqueda(i, j + 1, matriz)
        Busqueda(i + 1, j + 1, matriz)
        Busqueda(i + 1, j, matriz)
        Busqueda(i + 1, j - 1, matriz)
        Busqueda(i, j - 1, matriz)
        Busqueda(i - 1, j - 1, matriz)
