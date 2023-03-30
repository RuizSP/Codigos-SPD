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
    rowNumber = len(matriz1)
    colNumber = len(matriz2[0])
    matrizR = [[0 for j in range(colNumber)] for i in range(rowNumber)]
    return matrizR

def CalcLinhaMatriz(matriz1, matriz2, matrizR, i, num_threads):
    linhas_por_thread = int(len(matriz1) / num_threads)
    start = i * linhas_por_thread
    end = start + linhas_por_thread if i < num_threads - 1 else len(matriz1)
    for row in range(start, end):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                matrizR[row][j] += matriz1[row][k] * matriz2[k][j]

def multiplicaMatriz(matriz1, matriz2, num_threads=1):
    matrizR = criaResultante(matriz1, matriz2)
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=CalcLinhaMatriz, args=(matriz1, matriz2, matrizR, i, num_threads))
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
    return matrizR

def main():
    colA = 512
    rowA = 512
    colB = 64
    rowB = 512
    matrizA = criaMatriz(colA, rowA)
    matrizB = criaMatriz(colB, colB)
    
    tempo1 = time.time()     
    matrizR = multiplicaMatriz(matrizA, matrizB, num_threads=2)
    tempo2= time.time()

    print("-------------------------------------------------- Feito em paralelo------------------------------------------------------------")
    for row in range(len(matrizR)):
        print(matrizR[row])

    print(tempo2-tempo1)

if __name__ == '__main__':
    main()
