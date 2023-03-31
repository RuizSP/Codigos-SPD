import numpy as np
import time
import threading


# --------------------------------
#         Variaveis Globais
# --------------------------------
ROW_MATRIZ_A = 512
COL_MATRIZ_A = 512

ROW_MATRIZ_B = 512
COL_MATRIZ_B = 64

THREADS_NUMBER = 4

EXECUTIONS_NUMBER = 15

#                   Float
MATRIZ_A = np.random.rand(ROW_MATRIZ_A, COL_MATRIZ_A)
MATRIZ_B = np.random.rand(ROW_MATRIZ_B, COL_MATRIZ_B)

#                   Int
# MATRIZ_A = np.random.randint(low=0, high=10, size=(ROW_MATRIZ_A, COL_MATRIZ_A))
# MATRIZ_B = np.random.randint(low=0, high=10, size=(ROW_MATRIZ_B, COL_MATRIZ_B))


MATRIZ_C = np.zeros((ROW_MATRIZ_A, COL_MATRIZ_B))
# MATRIZ_C = np.zeros((ROW_MATRIZ_A, COL_MATRIZ_B), dtype=int)


EXECUTIONS_WITHOUT_THREAD = []
EXECUTIONS_WITH_THREAD = []


# --------------------------------
#         Verifica possibilidade de multiplicar
# --------------------------------
def is_possible_multiply():
    if (COL_MATRIZ_A != ROW_MATRIZ_B):
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
#         Multiplicação sem Thread
# --------------------------------


def multiply_matriz_without_thread():

    for i in range(ROW_MATRIZ_A):
        MATRIZ_C[i] = multiply_row(i)

# --------------------------------
#         Multiplicação com Thread
# --------------------------------


def multiply_matriz_with_thread(thread_id, worker_per_thread):
    for i in range(thread_id * worker_per_thread, worker_per_thread):
        MATRIZ_C[i] = multiply_row(i)


# --------------------------------
#         Imprimir matriz
# --------------------------------


def print_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

# --------------------------------
#         Antes de iniciar as execuções
# --------------------------------

# --------------------------------
#         Execução
# --------------------------------


def exec_without_thread():
    multiply_matriz_without_thread()


def exec_with_thread():
    threads = []
    work_per_thread = int(ROW_MATRIZ_A / THREADS_NUMBER)

    for i in range(THREADS_NUMBER):
        th = threading.Thread(
            target=multiply_matriz_with_thread,
            args=(i, work_per_thread))
        threads.append(th)
        th.start()

    for i in threads:
        i.join()


def rotina_execucao_sem_thread():
    for i in range(EXECUTIONS_NUMBER):
        ini = time.time()
        exec_without_thread()
        fim = time.time()
        tempoExec = fim - ini
        EXECUTIONS_WITHOUT_THREAD.append(tempoExec)


def rotina_execucao_com_thread():
    for i in range(EXECUTIONS_NUMBER):
        ini = time.time()
        exec_with_thread()
        fim = time.time()
        tempoExec = fim - ini
        EXECUTIONS_WITH_THREAD.append(tempoExec)

# --------------------------------
#         Speed up
# --------------------------------


def mediaTempo(temposExec):
    somatorio = 0
    for i in range(len(temposExec)):
        somatorio += temposExec[i]
    return somatorio/len(temposExec)


def Speedup():
    mediaSem = mediaTempo(EXECUTIONS_WITHOUT_THREAD)
    print("Media sem \t--> ", mediaSem)

    mediaCom = mediaTempo(EXECUTIONS_WITH_THREAD)
    print("Media com \t--> ", mediaCom)

    return mediaSem / mediaCom


def start():
    rotina_execucao_sem_thread()
    rotina_execucao_com_thread()
    print("SpeedUp \t--> ", Speedup())

# --------------------------------
#         Main
# --------------------------------


def main():
    start()


if __name__ == "__main__":
    main()
