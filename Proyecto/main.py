import time
import itertools

MAYOR = 0
MENORIGUAL = 1

def comparacionesDimension(dimension):
    l=[list(e) for e in itertools.product(*[[MAYOR,MENORIGUAL] for x in range(dimension)])]
    l.sort()
    return l

"""
    n*(2^r)*r
    No se pueden tener puntos duplicados en la lista de puntos al momento de crear
"""
def crearArbol(puntos,dimension):
    operandos = comparacionesDimension(dimension)
    largoOperandos = len(operandos)
    return crearArbolRecursivo(puntos,dimension,operandos,largoOperandos)

def crearArbolRecursivo(puntos,dimension,operandos,largoOperandos):
    if not puntos:
        return None
    elif len(puntos) == 1:
        return puntos
    largoPuntos = len(puntos)
    medianas = [sum([x[i] for x in puntos])//largoPuntos for i in range(dimension)]
    auxiliares = [[] for x in range(largoOperandos)]
    for i in puntos:
        for c in range(largoOperandos):
            for m in range(dimension):
                if operandos[c][m] == MAYOR:
                    if i[m] <= medianas[m]:
                        break
                else:
                    if i[m] > medianas[m]:
                        break
            else:
                auxiliares[c].append(i)
                break
    resultado = [crearArbolRecursivo(a,dimension,operandos,largoOperandos) for a in auxiliares]
    return (medianas,resultado)

"""
    (2^r)*r
"""
def buscar(arbol,punto,r):
    operandos = comparacionesDimension(r)
    largoOperandos = len(operandos)
    dimension = len(arbol[0])
    return buscarRecursivo(arbol,punto,operandos,largoOperandos,dimension)

def buscarRecursivo(arbol,punto,operandos,largoOperandos,dimension):
    if arbol == None:
        return False
    elif len(arbol) == 1:
        return punto == arbol[0]
    for c in range(largoOperandos):
        for m in range(dimension):
            if operandos[c][m] == MAYOR:
                if punto[m] <= arbol[0][m]:
                    break
            else:
                if punto[m] > arbol[0][m]:
                    break
        else:
            return buscarRecursivo(arbol[1][c],punto,operandos,largoOperandos,dimension)
    return False

import random

r=3
for k in [20]:
    if k<3:
        r=k
    else:
        r=3
    print("Start "+str(k)+" using "+str(r))
    for n in [1000000]:
        random.seed(30)
        print("N "+str(n))
        puntos = []
        start = time.perf_counter()

        pDim = []
        for d in range(k):
            choices = list(range(n))
            random.shuffle(choices)
            pDim.append(choices)
        for i in range(n):
            p=[]
            for d in range(k):
                p.append(pDim[d][i])
            puntos.append(p)
        elapsed = time.perf_counter()
        print("--- Generacion puntos %s segundos ---" % (elapsed-start))
        start = time.perf_counter()
        arbol = crearArbol(puntos,r)
        elapsed = time.perf_counter()
        print("--- Creacion arbol %s segundos ---" % (elapsed-start))

        tiemposBusquedaAcierto=[]
        tiemposBusquedaIncierta=[]
        print("Inicio busqueda aciertos")
        for p in range(100):
            start = time.perf_counter()
            buscar(arbol,puntos[p],r)
            elapsed = time.perf_counter()
            tiemposBusquedaAcierto.append(elapsed-start)
        i=0
        print("--- Busqueda aciertos %s segundos ---" % (sum(tiemposBusquedaAcierto)/len(tiemposBusquedaAcierto)))
        random.seed(70)
        print("Inicio busqueda inciertos")

        while i<100:
            while True:
                p=[]
                for d in range(k):
                    p.append(random.randint(0,10000))
                if p not in puntos:
                    start = time.perf_counter()
                    buscar(arbol,p,r)
                    elapsed = time.perf_counter()
                    tiemposBusquedaIncierta.append(elapsed-start)
                    break
            i+=1
        print("--- Busqueda inciertos %s segundos ---" % (sum(tiemposBusquedaIncierta)/len(tiemposBusquedaIncierta)))
        print("--- Busqueda total %s segundos ---" % ((sum(tiemposBusquedaAcierto)+sum(tiemposBusquedaIncierta))/(len(tiemposBusquedaIncierta)+len(tiemposBusquedaAcierto))))
        print(" === ")

#print("======BUSQUEDA=======")
#print(buscar(arbol,[4760,10479]))
