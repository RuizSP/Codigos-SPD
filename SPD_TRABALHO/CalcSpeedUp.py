import subprocess

EXECUTIONS_NUMBER = 15

ROW_MATRIZ_A = 32
COL_MATRIZ_A = 32

ROW_MATRIZ_B = 32
COL_MATRIZ_B = 32

THREADS_NUMBER = 1

DELIMITADOR = '|'

HISTORICO_SEM_THREAD = []
HISTORICO_COM_2_THREAD = []
HISTORICO_COM_4_THREAD = []
HISTORICO_COM_8_THREAD = []

INPUT_SEQUENCIAL = (str(ROW_MATRIZ_A) + DELIMITADOR +
                    str(COL_MATRIZ_A) + DELIMITADOR +
                    str(ROW_MATRIZ_B) + DELIMITADOR +
                    str(COL_MATRIZ_B) + DELIMITADOR)

INPUT_PARALELO = (str(ROW_MATRIZ_A) + DELIMITADOR +
                  str(COL_MATRIZ_A) + DELIMITADOR +
                  str(ROW_MATRIZ_B) + DELIMITADOR +
                  str(COL_MATRIZ_B) + DELIMITADOR +
                  str(THREADS_NUMBER))

# Subprocess para o algoritmo sequencial
args_sequencial = ['python3', 'MultSequecial.py']
subProc_sequencial = subprocess.Popen(args_sequencial,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      text=True)

# Subprocess para o algoritmo paralelo
args_paralelo = ['python3', 'MultParalelo.py']
subProc_paralelo = subprocess.Popen(args_paralelo,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)


def calculoMedia(vetor_valores):
    total = 0
    for i in vetor_valores:
        total += i
    return total / len(vetor_valores)


def rotina_execucoes_sem_thread():
    for i in range(EXECUTIONS_NUMBER):
        saida_sequecial = subProc_sequencial.communicate(INPUT_SEQUENCIAL)
        HISTORICO_SEM_THREAD.append(float(saida_sequecial[0]))
    print("Rotina sem thread finalizada")


def rotina_execucoes_com_thread(quantidade_thread):
    THREADS_NUMBER = quantidade_thread
    for i in range(EXECUTIONS_NUMBER):
        saida_paralelo = subProc_paralelo.communicate(INPUT_PARALELO)
        if quantidade_thread == 2:
            HISTORICO_COM_2_THREAD.append(float(saida_paralelo[0]))
        elif quantidade_thread == 4:
            HISTORICO_COM_2_THREAD.append(float(saida_paralelo[0]))
        elif quantidade_thread == 8:
            HISTORICO_COM_2_THREAD.append(float(saida_paralelo[0]))
        else:
            exit()
    print("Rotina com " + str(quantidade_thread) + " threads finalizada")


def main():
    rotina_execucoes_sem_thread()
    rotina_execucoes_com_thread(2)
    rotina_execucoes_com_thread(4)
    rotina_execucoes_com_thread(8)
    print("-----------SEM THREAD-------------")
    print(HISTORICO_SEM_THREAD)

    print("\n Media: ", calculoMedia(HISTORICO_SEM_THREAD))
    print("----------------------------------")

    print("-----------2 THREAD-------------")
    print(HISTORICO_COM_2_THREAD)

    print("\n Media: ", calculoMedia(HISTORICO_COM_2_THREAD))
    print("----------------------------------")

    print("-----------4 THREAD-------------")
    print(HISTORICO_COM_4_THREAD)

    print("\n Media: ", calculoMedia(HISTORICO_COM_4_THREAD))
    print("----------------------------------")

    print("-----------8 THREAD-------------")
    print(HISTORICO_COM_8_THREAD)

    print("\n Media: ", calculoMedia(HISTORICO_COM_8_THREAD))
    print("----------------------------------")


if __name__ == "__main__":
    main()
