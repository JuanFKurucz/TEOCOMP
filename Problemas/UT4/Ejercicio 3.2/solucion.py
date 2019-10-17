import math
import time
import random

def binarySearch(A, x):
    comparaciones = 0
    asignaciones = 3
    operaciones = 1

    min = 0
    max = len(A)-1
    mid = 0
    while min <= max:
        comparaciones += 1
        mid = (min+max)//2
        asignaciones+=1
        operaciones+=1
        if x == A[mid]:
            comparaciones += 1
            print("Asignaciones: %i, Operaciones: %i, Comparaciones: %i, Total: %i" % (asignaciones,operaciones,comparaciones,(asignaciones+operaciones+comparaciones)))
            return mid
        elif x > A[mid]:
            comparaciones += 2
            min = mid + 1
            asignaciones+=1
            operaciones+=1
        else:
            comparaciones += 2
            max = mid - 1
            asignaciones+=1
            operaciones+=1
    print("Asignaciones: %i, Operaciones: %i, Comparaciones: %i, Total: %i" % (asignaciones,operaciones,comparaciones,(asignaciones+operaciones+comparaciones)))
    return -1


def interpolationSearch(A, x):
    comparaciones = 0
    asignaciones = 3
    operaciones = 1

    min = 0
    max = len(A)-1
    mid = 0
    while min < max:
        comparaciones += 1
        mid = (math.trunc((x-A[min])/(A[max]-A[min])   *   (max-min)))   +   min
        operaciones += 7
        asignaciones+=1
        if mid >= len(A):
            return -1
        if x == A[mid]:
            comparaciones += 1
            print("Asignaciones: %i, Operaciones: %i, Comparaciones: %i, Total: %i" % (asignaciones,operaciones,comparaciones,(asignaciones+operaciones+comparaciones)))
            return mid
        elif x > A[mid]:
            comparaciones += 2
            asignaciones+=1
            operaciones += 1
            min = mid + 1
        else:
            comparaciones += 2
            asignaciones+=1
            operaciones += 1
            max = mid - 1
    print("Asignaciones: %i, Operaciones: %i, Comparaciones: %i, Total: %i" % (asignaciones,operaciones,comparaciones,(asignaciones+operaciones+comparaciones)))
    return -1

def prueba(A,x):
    print("=======================")
    print("==Busqueda de %i==" % x)
    print(A)
    start = time.perf_counter()
    print(binarySearch(A,x))
    elapsed = time.perf_counter()
    elapsed = elapsed - start
    print("--- Binary %s segundos ---" % (elapsed))
    start = time.perf_counter()
    print(interpolationSearch(A,x))
    elapsed = time.perf_counter()
    elapsed = elapsed - start
    print("--- Interpolation %s segundos ---" % (elapsed))


def generarLista(cantidadNumeros,min,max):
    lista = []
    for n in range(cantidadNumeros):
        lista.append(random.randint(min, max))
    lista.sort()
    lista = list(dict.fromkeys(lista))
    return lista

for i in range(10):
    prueba(generarLista(10,1,50),random.randint(0, 50))
