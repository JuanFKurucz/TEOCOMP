import random
import time


def minDeMaxOutput(matriz):
    comparaciones = 0
    asignaciones = 1
    min = float('inf')
    for lista in matriz:
        comparaciones += 1
        asignaciones += 2
        max = float('-inf')
        for i in lista:
            asignaciones += 1
            comparaciones += 1
            if i>max:
                asignaciones += 1
                comparaciones += 1
                max=i
        if max<min:
            asignaciones += 1
            comparaciones += 1
            min = max
    print("Comparaciones: %i, Asignaciones: %i, Total: %i" % (comparaciones,asignaciones,(comparaciones+asignaciones)))
    return min

def minDeMax(matriz):
    min = float('inf')
    for lista in matriz:
        max = float('-inf')
        for i in lista:
            if i>max:
                max=i
        if max<min:
            min = max
    return min


def generarLista(cantidadListas,cantidadNumeros,min,max):
    lista = []
    for i in range(cantidadListas):
        lista.append([])
        for n in range(cantidadNumeros):
            lista[i].append(random.randint(min, max))
    return lista

def prueba(listas,numeros):
    print("Cantidad listas: %i" % listas)
    print("Cantidad numeros: %i" % numeros)
    matriz = generarLista(listas,numeros,-100,100)
    print("Arranco")
    start = time.perf_counter()
    print(minDeMax(matriz))
    elapsed = time.perf_counter()
    elapsed = elapsed - start
    print("--- %s segundos ---" % (elapsed))

for i in range(1,10):
    prueba(200,50)
    prueba(2000,50)
    prueba(20000,50)
    print("=============================================")
