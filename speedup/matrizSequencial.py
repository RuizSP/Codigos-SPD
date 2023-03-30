from random import randint
import time
import threading

def criaMatriz(col, row):
           matriz = [[0 for j in range(col)] for i in range(row)]
           for i in range(len(matriz)):
                      for j in range(len(matriz[0])):
                                 matriz[i][j] = randint(0,10)
           return matriz


def criaResultante(matriz1, matriz2):
# a funcao cria uma matriz resultante de forma dinamica de acordo com as matrizes entradas    
# por  conta das propriedade da  multipĺicação de matrizes, a matriz resultante tera o mesmo numero de linhas da matriz1
# e o mesmo numero de colunas da matriz 2.
    rowNumber = len(matriz1)
    colNumber = len(matriz2[0])
    matrizR = [[0 for j in range(colNumber)] for i in range(rowNumber)]
    return matrizR

#-------planejamento-----------
# primeira posicao da coluna da matriz resultante
# 1*0 + 0*1 + 2*-1 = -2
# segunda posicao da coluna da matriz resultante
# 0* 0 + 3 * 1 + 1*-1 = 2 
#pega a primeira linha da matriz 1, multiplica pela primeira coluna da mattriz 2.
#pega a segunda linha da matriz 1,  multiplica pela primeira coluna da mattriz 2, assim por diante.
#multiplica cada elemento da linha atual da matriz1 pelo elemento correspondente na coluna atual da matriz2 e soma todos esses produtos. O resultado é armazenado na matriz resultante.


def multiplicaMatriz(matriz1, matriz2):
    matrizR = criaResultante(matriz1, matriz2)
    for i in range(len(matriz1)): # for utilizando o numero de linhas da matriz 1.
        for j in range(len(matriz2[0])): # for com o numero de colunas da matriz 2. considerando que a matriz tem o mesmo numero de colunas em cada linha ele pega a quantidade de colunas na primeira linha
            for k in range(len(matriz2)): # for com o numero de linhas da matriz 2.
                    matrizR[i][j] += matriz1[i][k]* matriz2[k][j]

    for row in range(len(matrizR)):
        print(matrizR[row])
    # esta funcao tem tres for aninhados para percorrer cada linha da primeira matriz 
    # e para cada linha dela percorrer cada elemento 
    # da coluna da segunda matriz realiza a multiplicação do elemento [i][j] da matriz1 pelo elemento[k][j] da matriz 2
    # e soma com valor presente na posicao [i][j] da matrizR   
def CalcLinhaMatriz (matriz1, matriz2, matrizR, i):     
        
    if i == 0:
        for row in range(int(len(matriz1)/2)):
            for j in range(len(matriz2[0])):
                for k in range(len(matriz2)):
                    matrizR[row][j] += matriz1[row][k] * matriz2[k][j]
    elif i==1:
         for row in range((int(len(matriz1)/2)), len(matriz1)):
            for j in range(len(matriz2[0])):
                for k in range(len(matriz2)):
                    matrizR[row][j] += matriz1[row][k] * matriz2[k][j]
    

def main():
    colA = 1000
    rowA = 1000
    colB = 1000
    rowB = 1000
    matrizA = criaMatriz(colA, rowA)
    matrizB = criaMatriz(colB, colB)
    matrizR = criaResultante(matrizA, matrizB) 
   # tempo1 = time.time()     
    #multiplicaMatriz(matrizA, matrizB)
    tempo2= time.time()
    
    threads = []

    for i in range(2):
        t = threading.Thread(target = CalcLinhaMatriz, args= (matrizA, matrizB, matrizR, i))
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
    tempo3 = time.time()
    
    print("-------------------------------------------------- Feito em paralelo------------------------------------------------------------")
    for row in range(len(matrizR)):
        print(matrizR[row])
   # print(tempo2-tempo1)
    print(tempo3-tempo2)

if __name__ == '__main__':
    main()
