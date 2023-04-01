import numpy as np
import time
import threading

# --------------------------------
#         Variaveis Globais
# --------------------------------
ROW_MATRIZ_A, COL_MATRIZ_A, ROW_MATRIZ_B, COL_MATRIZ_B = 512, 512, 512, 64


THREADS_NUMBER = 2


MATRIZ_A = np.random.randint(
    size=(ROW_MATRIZ_A, COL_MATRIZ_A), low=-100, high=101)
MATRIZ_B = np.random.randint(
    size=(ROW_MATRIZ_B, COL_MATRIZ_B), low=-100, high=101)
MATRIZ_C = np.zeros((ROW_MATRIZ_A, COL_MATRIZ_B))

# --------------------------------
#         Verifica possibilidade de multiplicar
# --------------------------------


def is_possible_multiply(matriz_A, matriz_B):
    if (len(matriz_A[0]) != len(matriz_B)):
        print("Não vai ser possivel multiplicar as duas matrizes")
        exit()

# --------------------------------
#         Multiplicação da linha
# --------------------------------


def multiply_row(row):

    for i in range(COL_MATRIZ_B):
        for j in range(ROW_MATRIZ_B):
            MATRIZ_C[row][i] += MATRIZ_A[row][j] * MATRIZ_B[j][i]

# --------------------------------
#         Multiplicação sem Thread
# --------------------------------


def multiply_matriz(thread_id, work_per_thread):
    for i in range(thread_id * work_per_thread, thread_id * work_per_thread + work_per_thread):
        MATRIZ_C[i] = multiply_row(i)


def exec():
    threads = []
    work_per_thread = int(ROW_MATRIZ_A / THREADS_NUMBER)

    for i in range(THREADS_NUMBER):
        th = threading.Thread(
            target=multiply_matriz,
            args=(i, work_per_thread))
        threads.append(th)
        th.start()

    for i in threads:
        i.join()

# --------------------------------
#         Imprimir matriz
# --------------------------------


def print_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


# ---------------------------------------
def create_random_matriz(row, col):
    return np.random.randint(low=-100, high=101, size=(row, col))


# ---------------------------------------


# --------------------------------
#         Main
# --------------------------------


def main():
    is_possible_multiply(MATRIZ_A, MATRIZ_B)

    inicio = time.time()

    exec()

    fim = time.time()

    tempo_execution = fim - inicio
    print(tempo_execution)


if __name__ == "__main__":
    main()
