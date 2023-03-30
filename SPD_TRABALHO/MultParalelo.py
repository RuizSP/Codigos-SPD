import numpy as np
import time
import threading


# --------------------------------
#         Variaveis Globais
# --------------------------------
ROW_MATRIZ_A, COL_MATRIZ_A, ROW_MATRIZ_B, COL_MATRIZ_B, THREADS_NUMBER = 1, 1, 1, 1, 1
DELIMITADOR = '|'

#                   Float
MATRIZ_A = np.random.rand(ROW_MATRIZ_A, COL_MATRIZ_A)
MATRIZ_B = np.random.rand(ROW_MATRIZ_B, COL_MATRIZ_B)
MATRIZ_C = np.zeros((ROW_MATRIZ_A, COL_MATRIZ_B))

#                   Int
# MATRIZ_A = np.random.randint(low=0, high=10, size=(ROW_MATRIZ_A, COL_MATRIZ_A))
# MATRIZ_B = np.random.randint(low=0, high=10, size=(ROW_MATRIZ_B, COL_MATRIZ_B))
# MATRIZ_C = np.zeros((ROW_MATRIZ_A, COL_MATRIZ_B), dtype=int)


# --------------------------------
#         Verifica possibilidade de multiplicar
# --------------------------------


def is_possible_multiply(matriz_A, matriz_B):
    if (len(matriz_A[0]) != len(matriz_B)):
        print("Não vai ser possivel multiplicar as duas matrizes")
        exit()


# --------------------------------
#         Multiplicação da linha, pode ser usada em todos os casos
# --------------------------------


def multiply_row(row):
    result_row = np.zeros(COL_MATRIZ_B)
    for i in range(COL_MATRIZ_B):
        for j in range(ROW_MATRIZ_B):
            result_row[i] += MATRIZ_A[row][j] * MATRIZ_B[j][i]
    return result_row


# --------------------------------
#         Multiplicação com Thread
# --------------------------------


def multiply_matriz(thread_id, worker_per_thread):
    for i in range(thread_id * worker_per_thread, worker_per_thread + thread_id * worker_per_thread):
        MATRIZ_C[i] = multiply_row(i)

# --------------------------------
#         Cria e inicia as threads
# --------------------------------


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
# --------------------------------plit(input())

def main():

    parametros_entrada = input()
    valores_entrada = parametros_entrada.split(DELIMITADOR)

    row_matriz_A = int(valores_entrada[0])
    col_matriz_A = int(valores_entrada[1])
    row_matriz_B = int(valores_entrada[2])
    col_matriz_B = int(valores_entrada[3])

    matriz_A = create_random_matriz(row_matriz_A, col_matriz_A)
    matriz_B = create_random_matriz(row_matriz_B, col_matriz_B)

    is_possible_multiply(matriz_A, matriz_B)

    inicio = time.time()
    exec()
    fim = time.time()

    tempo_execution = fim - inicio
    print(tempo_execution)


if __name__ == "__main__":
    main()
