import cv2
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm.Get_rank()

localimage = None
newimage = None
image = None
newLocalImage = None
n =0
largura = 0

if myrank == 0:
    image = cv2.imread("maspcomruido.jpg", 0) #trabalhando com imagem de um canal (escala de cinza)
    altura, largura = image.shape
    n = int(altura/nprocs)
    newimage = np.zeros((altura, largura),dtype = 'uint8')
    

(n, largura) = comm.bcast((n,largura), root =0)
localimage = np.zeros((n,largura), dtype='uint8')
newLocalImage = np.zeros((n, largura),dtype = 'uint8')

#Distribuindo entre processos:
comm.Scatterv(image, localimage, root =0)
cv2.imshow("corte", localimage)

#print(image.dtype.type)

# Filtro média 3x3
for y in range(1, n - 1):
    for x in range(1, largura - 1):
        media = int(localimage[y - 1][x - 1]) + int(localimage[y - 1][x]) + int(localimage[y - 1][x + 1]) #1º linha
        media += int(localimage[y][x - 1]) + int(localimage[y][x]) + int(localimage[y][x + 1])             #2º linha
        media += int(localimage[y + 1][x - 1]) + int(localimage[y + 1][x]) + int(localimage[y + 1][x + 1]) #3º linha

        media = int(media / 9)

        newLocalImage[y][x] = media
 
comm.Gatherv(newLocalImage, newimage, root=0)
#cv2.imshow("CORTE", finalImage)

if myrank ==0:
    cv2.imshow("original image", image)
    cv2.imshow("filtered image", newimage)


cv2.waitKey(0)
cv2.destroyAllWindows()