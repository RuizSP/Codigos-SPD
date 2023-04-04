import numpy as np
import time

# --------------------------------
#         Variaveis Globais
# --------------------------------
ROW_MATRIZ_A, COL_MATRIZ_A, ROW_MATRIZ_B, COL_MATRIZ_B = 512, 512, 512, 64

MATRIZ_A = np.random.randint(
    low=-100, high=101, size=(ROW_MATRIZ_A, COL_MATRIZ_A))
MATRIZ_B = np.random.randint(
    low=-100, high=101, size=(ROW_MATRIZ_B, COL_MATRIZ_B))
MATRIZ_C = np.zeros((ROW_MATRIZ_A, COL_MATRIZ_B), dtype=int)


# --------------------------------
#         Multiplicação da matriz
# --------------------------------

def multiply_matriz():
    for i in range(ROW_MATRIZ_A):
        for j in range(COL_MATRIZ_B):
            for k in range(ROW_MATRIZ_B):
                MATRIZ_C[i][j] += MATRIZ_A[i][k] * MATRIZ_B[k][j]

# --------------------------------
#         Imprimir matriz
# --------------------------------


def print_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

# --------------------------------
#         Main
# --------------------------------


def main():

    inicio = time.time()

    multiply_matriz()

    fim = time.time()

    tempo_execution = fim - inicio
    print(tempo_execution)


if __name__ == "__main__":
    main()
