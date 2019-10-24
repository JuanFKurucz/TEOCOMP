import time
import random

def thirdSort(A, first, last):
    if A[first] > A[last]:
        temp = A[first]
        A[first] = A[last]
        A[last] = temp

    if first + 1 < last:
        pivot = (last - first + 1)//3
        thirdSort(A, first, last - pivot)
        thirdSort(A, first + pivot, last)
        thirdSort(A, first, last - pivot)

def mergeSort(A,p,r):
    if p < r:
        q = (p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = list(range(1,n1+2))
    R = list(range(1,n2+2))
    for i in range(1,n1):
        L[i] = A[p+i-1]
    for j in range(1,n2):
        R[j] = A[q+j]
    L.append(float("inf"))
    R.append(float("inf"))
    i = 1
    j = 1
    for k in range(p,r):
        if L[i] <= R[j]:
            print(L[i])
            A[k] = L[i]
            i+=1
        else:
            print("" % (k,j,A[k],R[j]))
            A[k] = R[j]
            j+=1
        print(A)

def prueba():
    print("=======================")
    tiempos = []
    for i in range(3):
        lista = generarLista(1000,0,5)
        print(lista)
        start = time.perf_counter()
        #mergeSort(lista,0,len(lista))
        #thirdSort(lista,0,len(lista)-1)
        elapsed = time.perf_counter()
        tiempos.append(elapsed - start)
        print(lista)
    promedioTiempo = sum(tiempos) / float(len(tiempos))
    print("--- thirdSort %s segundos ---" % (promedioTiempo))


def generarLista(cantidadNumeros,min,max):
    lista = []
    for n in range(cantidadNumeros):
        lista.append(random.randint(min, max))
    return lista

#prueba()
lista = [5,1]
mergeSort(lista,0,len(lista))
print(lista)
