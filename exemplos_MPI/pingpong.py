import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = numpy.zeros(1)

if rank ==1:
    randNum = numpy.random.random_sample(1)
    print("Processo ",rank, " escreveu o numero ", randNum[0] )
    comm.Send(randNum, dest = 0)

if rank ==0:
    print("Processo ", rank, "antes de receber, tem o numero ", randNum[0])
    comm.Recv(randNum, source=1)
    print("processo ", rank, "recebeu o numero ", randNum[0])
