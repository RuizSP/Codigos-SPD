import subprocess

EXECUTIONS_NUMBER = 1

ROW_MATRIZ_A = 512
COL_MATRIZ_A = 512

ROW_MATRIZ_B = 512
COL_MATRIZ_B = 64

DELIMITADOR = '|'


# Subprocess para o algoritmo sequencial
args_sequencial = ['python3', 'MultSequecial.py']


# Subprocess para o algoritmo paralelo
args_paralelo = ['python3', 'MultParalelo.py']


def calculoMedia(vetor_valores):
    total = 0
    for i in vetor_valores:
        total += i
    return total / len(vetor_valores)


def rotina_execucoes_sem_thread(historico):
    print("Rotina sem thread iniciada")
    input_sequencial = (str(ROW_MATRIZ_A) + DELIMITADOR +
                        str(COL_MATRIZ_A) + DELIMITADOR +
                        str(ROW_MATRIZ_B) + DELIMITADOR +
                        str(COL_MATRIZ_B) + DELIMITADOR)

    for i in range(EXECUTIONS_NUMBER):
        processo = subprocess.Popen(args_sequencial,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)

        processo.stdin.write(input_sequencial)

        saida_sequencial = processo.communicate()

        processo.stdin.close()

        historico.append(float(saida_sequencial[0]))

        print("---> Teste " + str(i+1) + "\t| Finalizado. tempo: " +
              str(float(saida_sequencial[0])))

    print("Rotina sem thread finalizada")
    print("----------------------------------------------------------------------------")


def rotina_execucoes_com_thread(quantidade_thread, historico):
    print("Rotina com " + str(quantidade_thread) + " thread iniciada")

    input_paralelo = (str(ROW_MATRIZ_A) + DELIMITADOR +
                      str(COL_MATRIZ_A) + DELIMITADOR +
                      str(ROW_MATRIZ_B) + DELIMITADOR +
                      str(COL_MATRIZ_B) + DELIMITADOR +
                      str(quantidade_thread))

    for i in range(EXECUTIONS_NUMBER):
        processo = subprocess.Popen(args_paralelo,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)

        processo.stdin.write(input_paralelo)

        saida_paralelo = processo.communicate()

        processo.stdin.close()

        historico.append(float(saida_paralelo[0]))

        print("---> Teste " + str(i+1) + "\t| Finalizado. tempo: " +
              str(float(saida_paralelo[0])))

    print("Rotina com " + str(quantidade_thread) + " threads finalizada")
    print("----------------------------------------------------------------------------")


def print_vetor(vetor):
    for i in vetor:
        print(i)


def main():

    historico_sem_thread = []
    historico_com_2_thread = []
    historico_com_4_thread = []
    historico_com_8_thread = []

    rotina_execucoes_sem_thread(historico_sem_thread)
    rotina_execucoes_com_thread(2, historico_com_2_thread)
    rotina_execucoes_com_thread(4, historico_com_4_thread)
    rotina_execucoes_com_thread(8, historico_com_8_thread)

    print("-----------SEM THREAD-------------")
    print_vetor(historico_sem_thread)

    print("\n Media: ", calculoMedia(historico_sem_thread))
    print("----------------------------------")

    print("-----------2 THREAD-------------")
    print_vetor(historico_com_2_thread)

    print("\n Media: ", calculoMedia(historico_com_2_thread))
    print("----------------------------------")

    print("-----------4 THREAD-------------")
    print_vetor(historico_com_4_thread)

    print("\n Media: ", calculoMedia(historico_com_4_thread))
    print("----------------------------------")

    print("-----------8 THREAD-------------")
    print_vetor(historico_com_8_thread)

    print("\n Media: ", calculoMedia(historico_com_8_thread))
    print("----------------------------------")


if __name__ == "__main__":
    main()
