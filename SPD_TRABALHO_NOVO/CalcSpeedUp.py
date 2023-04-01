import subprocess

EXECUTIONS_NUMBER = 25

args_sequencial = ['python3', 'MultSequecial.py']
args_paralelo2 = ['python3', 'MultParalelo2.py']
args_paralelo4 = ['python3', 'MultParalelo4.py']
args_paralelo8 = ['python3', 'MultParalelo8.py']


def calculoMedia(vetor_valores):
    total = 0
    for i in vetor_valores:
        total += i
    return total / len(vetor_valores)


def rotina_execucoes_sem_thread(historico):
    print("Rotina sem thread iniciada")

    for i in range(EXECUTIONS_NUMBER):
        processo = subprocess.Popen(args_sequencial,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)

        saida_sequencial = processo.communicate()

        processo.stdin.close()

        historico.append(float(saida_sequencial[0]))

        print("---> Teste " + str(i+1) + "\t| Finalizado. tempo: " +
              str(float(saida_sequencial[0])))

    print("Rotina sem thread finalizada")
    print("----------------------------------------------------------------------------")


def rotina_execucoes_com_2_thread(historico):
    print("Rotina com 2 thread iniciada")

    for i in range(EXECUTIONS_NUMBER):

        processo = subprocess.Popen(args_paralelo2,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)

        saida_paralelo = processo.communicate()

        processo.stdin.close()

        historico.append(float(saida_paralelo[0]))

        print("---> Teste " + str(i+1) + "\t| Finalizado. tempo: " +
              str(float(saida_paralelo[0])))

    print("Rotina com 2 threads finalizada")
    print("----------------------------------------------------------------------------")


def rotina_execucoes_com_4_thread(historico):
    print("Rotina com 4 thread iniciada")

    for i in range(EXECUTIONS_NUMBER):

        processo = subprocess.Popen(args_paralelo4,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)

        saida_paralelo = processo.communicate()

        processo.stdin.close()

        historico.append(float(saida_paralelo[0]))

        print("---> Teste " + str(i+1) + "\t| Finalizado. tempo: " +
              str(float(saida_paralelo[0])))

    print("Rotina com 4 threads finalizada")
    print("----------------------------------------------------------------------------")


def rotina_execucoes_com_8_thread(historico):
    print("Rotina com 8 thread iniciada")

    for i in range(EXECUTIONS_NUMBER):

        processo = subprocess.Popen(args_paralelo8,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)

        saida_paralelo = processo.communicate()

        processo.stdin.close()

        historico.append(float(saida_paralelo[0]))

        print("---> Teste " + str(i+1) + "\t| Finalizado. tempo: " +
              str(float(saida_paralelo[0])))

    print("Rotina com 8 threads finalizada")
    print("----------------------------------------------------------------------------")


def speed_up(tempo1, tempo2):
    return tempo1 / tempo2


def print_vetor(vetor):
    for i in vetor:
        print(i)


def main():

    historico_sem_thread = []
    historico_com_2_thread = []
    historico_com_4_thread = []
    historico_com_8_thread = []

    rotina_execucoes_sem_thread(historico_sem_thread)
    rotina_execucoes_com_2_thread(historico_com_2_thread)
    rotina_execucoes_com_4_thread(historico_com_4_thread)
    rotina_execucoes_com_8_thread(historico_com_8_thread)

    print("-----------SEM THREAD-------------")
    print_vetor(historico_sem_thread)

    print("----------------------------------")

    print("-----------2 THREAD-------------")
    print_vetor(historico_com_2_thread)

    print("----------------------------------")

    print("-----------4 THREAD-------------")
    print_vetor(historico_com_4_thread)

    print("----------------------------------")

    print("-----------8 THREAD-------------")
    print_vetor(historico_com_8_thread)

    print("----------------------------------")
    print("--------------------------------------------------------------------")

    mediaSemThread = calculoMedia(historico_sem_thread)
    media2thread = calculoMedia(historico_com_2_thread)
    media4thread = calculoMedia(historico_com_4_thread)
    media8thread = calculoMedia(historico_com_8_thread)

    print("\n Media Sem Thread: ", mediaSemThread)
    print("\n Media 2 Thread: ", media2thread)
    print("\n Media 4 Thread: ", media4thread)
    print("\n Media 8 Thread: ", media8thread)
    print("--------------------------------------------------------------------")
    print("\n SpeedUp (sequencial vs 2 threads): ",
          speed_up(mediaSemThread, media2thread))
    print("\n SpeedUp (sequencial vs 4 threads): ",
          speed_up(mediaSemThread, media4thread))
    print("\n SpeedUp (sequencial vs 8 threads): ",
          speed_up(mediaSemThread, media8thread))
    print("--------------------------------------------------------------------")


if __name__ == "__main__":
    main()
