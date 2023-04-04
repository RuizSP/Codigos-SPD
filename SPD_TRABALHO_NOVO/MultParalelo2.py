import numpy as np
import time
import threading

# --------------------------------
#         Variaveis Globais
# --------------------------------
THREADS_NUMBER = 2

ROW_MATRIZ_A, COL_MATRIZ_A, ROW_MATRIZ_B, COL_MATRIZ_B = 512, 512, 512, 64

MATRIZ_A = np.random.randint(
    low=-100, high=101, size=(ROW_MATRIZ_A, COL_MATRIZ_A))
MATRIZ_B = np.random.randint(
    low=-100, high=101, size=(ROW_MATRIZ_B, COL_MATRIZ_B))
MATRIZ_C = np.zeros((ROW_MATRIZ_A, COL_MATRIZ_B), dtype=int)

# --------------------------------
#         Multiplicação da matriz
# --------------------------------


def multiply_row(i):
    for j in range(COL_MATRIZ_B):
        for k in range(ROW_MATRIZ_B):
            MATRIZ_C[i][j] += MATRIZ_A[i][k] * MATRIZ_B[k][j]


def multiply_matriz(thread_id, work_per_thread):
    for i in range(thread_id * work_per_thread, thread_id * work_per_thread + work_per_thread):
        multiply_row(i)


def exec():
    threads = []

    work_per_thread = ROW_MATRIZ_A // THREADS_NUMBER

    for i in range(THREADS_NUMBER):
        t = threading.Thread(
            target=multiply_matriz,
            args=(i, work_per_thread))
        threads.append(t)
        t.start()

    for i in threads:
        i.join()

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
    exec()
    fim = time.time()

    tempo_execution = fim - inicio
    print(tempo_execution)


if __name__ == "__main__":
    main()
