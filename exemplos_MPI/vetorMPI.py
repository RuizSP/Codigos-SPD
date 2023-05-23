import numpy
from mpi4py import MPI

TAMANHOVETOR = 10000
vetor = numpy.arange(TAMANHOVETOR) 

def soma(inicio, fim):
    s = numpy.zeros(1)
    for x in range(inicio, fim, 1):
        s = s + vetor[x]
    return s

comm = MPI.COMM_WORLD
nprocs =  comm.Get_size()
myrank = comm.Get_rank()

n = TAMANHOVETOR/nprocs 


total = numpy.zeros(1)
valor = soma(int(n*myrank), int(n*(myrank+1)-1))
comm.Reduce(valor, total, op=MPI.SUM, root=0)


if myrank ==0:
    print("A soma do vetor eh: ", total)