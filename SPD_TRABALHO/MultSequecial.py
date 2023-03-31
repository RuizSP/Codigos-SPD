import numpy as np
import time

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


def multiply_row(matriz_A_row, matriz_B):

    row_result = np.zeros(len(matriz_B[0]), dtype=int)
    for i in range(len(matriz_B[0])):
        for j in range(len(matriz_B)):
            row_result[i] += matriz_A_row[j] * matriz_B[j][i]
    return row_result

# --------------------------------
#         Multiplicação sem Thread
# --------------------------------


def multiply_matriz(matriz_A, matriz_B):
    matriz_result = np.zeros((len(matriz_A), len(matriz_B[0])), dtype=int)
    for i in range(len(matriz_A)):
        matriz_result[i] = multiply_row(matriz_A[i], matriz_B)
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

    matriz_A = create_random_matriz(row_matriz_A, col_matriz_A)
    matriz_B = create_random_matriz(row_matriz_B, col_matriz_B)

    is_possible_multiply(matriz_A, matriz_B)

    inicio = time.time()

    M = multiply_matriz(matriz_A, matriz_B)

    fim = time.time()

    tempo_execution = fim - inicio
    print(tempo_execution)


if __name__ == "__main__":
    main()
