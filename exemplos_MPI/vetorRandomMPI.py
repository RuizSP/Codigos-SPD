import numpy
from mpi4py import MPI

TAMANHOVETOR = 20
vetor = numpy.random.randint(0, 100, size=20)

def soma(inicio, fim):
    s = numpy.zeros(1)
    for x in range(inicio, fim):
        s += vetor[x]
    return s

comm = MPI.COMM_WORLD
nprocs = 4  # Definindo o número de processos como 4
myrank = comm.Get_rank()

n = TAMANHOVETOR // nprocs
resto = TAMANHOVETOR % nprocs

inicio = n * myrank
fim = inicio + n

# Distribui o resto de elementos entre os primeiros processos
if myrank < resto:
    inicio += myrank
    fim += myrank + 1
else:
    inicio += resto
    fim += resto

total = numpy.zeros(1)
valor = soma(inicio, fim)
comm.Reduce(valor, total, op=MPI.SUM, root=0)

if myrank == 0:
    print("A soma do vetor é:", total[0])