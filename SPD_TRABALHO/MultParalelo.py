import numpy as np
import time
import threading


# --------------------------------
#         Variaveis Globais
# --------------------------------
DELIMITADOR = '|'

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


def multiply_row(matriz_A_row, matriz_B, matriz_result_row):
    for i in range(len(matriz_B[0])):
        for j in range(len(matriz_B)):
            matriz_result_row[i] += matriz_A_row[j] * matriz_B[j][i]


# --------------------------------
#         Multiplicação com Thread
# --------------------------------


def multiply_matriz(thread_id, worker_per_thread, matriz_A, matriz_B, matriz_result):
    for i in range(thread_id * worker_per_thread, worker_per_thread + thread_id * worker_per_thread):
        multiply_row(matriz_A[i], matriz_B, matriz_result[i])

# --------------------------------
#         Cria e inicia as threads
# --------------------------------


def exec(matriz_A, matriz_B, thread_number):

    # para evitar bugs, a carga de trabalho tem que ser maior que 0 e thread diferete de 0
    if (thread_number < len(matriz_A)):
        work_per_thread = int(len(matriz_A) / thread_number)
    else:
        work_per_thread = 1
        thread_number = len(matriz_A)

    matriz_result = np.zeros((len(matriz_A), len(matriz_B[0])), dtype=int)

    threads = []

    for i in range(thread_number):
        th = threading.Thread(
            target=multiply_matriz,
            args=(i, work_per_thread, matriz_A, matriz_B, matriz_result))
        threads.append(th)
        th.start()
    for i in threads:
        i.join()

    return matriz_result

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

    parametros_entrada = input()
    valores_entrada = parametros_entrada.split(DELIMITADOR)

    row_matriz_A = int(valores_entrada[0])
    col_matriz_A = int(valores_entrada[1])
    row_matriz_B = int(valores_entrada[2])
    col_matriz_B = int(valores_entrada[3])
    thread_number = int(valores_entrada[4])

    matriz_A = create_random_matriz(row_matriz_A, col_matriz_A)
    matriz_B = create_random_matriz(row_matriz_B, col_matriz_B)

    is_possible_multiply(matriz_A, matriz_B)

    inicio = time.time()
    M = exec(matriz_A, matriz_B, thread_number)
    fim = time.time()

    tempo_execution = fim - inicio
    print(tempo_execution)


if __name__ == "__main__":
    main()
