import random
import time


def minDeMax(matriz):
    iteraciones = 0
    min = float('inf')
    max = float('-inf')
    for lista in matriz:
        iteraciones += 4
        for i in lista:
            iteraciones += 3
            if i>max:
                iteraciones += 1
                max=i
        if max<min:
            iteraciones += 1
            min = max
        max = float('-inf')
    print("Operaciones: %i" % iteraciones)
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

prueba(200,50)
prueba(2000,50)
prueba(20000,50)
