import time
import itertools
import random

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

def makeKDTree(points, dim = 0):
    if not points:
        return None # Empty trees are None
    elif len(points) == 1:
        return tuple(points) # Leaf nodes have one point.
    points.sort(key = lambda p: p[dim])
    medianIndex = len(points) // 2
    median = points[medianIndex][dim]
    nextDim = (dim + 1) % len(points[medianIndex])
    left = [p for p in points if p[dim] < median]
    right = [p for p in points if p[dim] >= median]
    return (median, makeKDTree(left, nextDim), makeKDTree(right, nextDim))

def searchKDTree(kdTree, point, dim = 0):
    if len(kdTree) == 1:
        return kdTree[0] == point
    nodeValue, left, right = kdTree
    nextDim = (dim + 1) % len(point)
    nextTree = left if point[dim] < nodeValue else right
    return searchKDTree(nextTree, point, nextDim)

r=3
for k in [5,10,15,20]:
    print("Start "+str(k)+" using "+str(r))
    for n in [100000,500000,1000000]:
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

        start = time.perf_counter()
        arbolCatedra = makeKDTree(puntos,r)
        elapsed = time.perf_counter()
        print("--- Creacion arbol CATEDRA %s segundos ---" % (elapsed-start))

        tiemposBusquedaAcierto=[]
        tiemposBusquedaIncierta=[]
        print("Inicio busqueda aciertos")
        for p in range(100):
            start = time.perf_counter()
            buscar(arbol,puntos[p],r)
            elapsed = time.perf_counter()
            tiemposBusquedaAcierto.append(elapsed-start)
        resultadoAciertos = sum(tiemposBusquedaAcierto)/len(tiemposBusquedaAcierto)
        print("--- Busqueda aciertos %s segundos ---" % (resultadoAciertos))

        tiemposBusquedaAciertoCatedra=[]
        tiemposBusquedaInciertaCatedra=[]
        for p in range(100):
            start = time.perf_counter()
            searchKDTree(arbolCatedra,puntos[p],r)
            elapsed = time.perf_counter()
            tiemposBusquedaAciertoCatedra.append(elapsed-start)
        resultadoAciertosCatedra = sum(tiemposBusquedaAciertoCatedra)/len(tiemposBusquedaAciertoCatedra)
        print("--- Busqueda aciertos CATEDRA %s segundos ---" % (resultadoAciertosCatedra))

        print("Inicio busqueda inciertos")
        i=0
        random.seed(70)
        while i<100:
            while True:
                p=[]
                for d in range(k):
                    p.append(random.randint(0,10000))
                if not buscar(arbol,p,r):
                    start = time.perf_counter()
                    buscar(arbol,p,r)
                    elapsed = time.perf_counter()
                    tiemposBusquedaIncierta.append(elapsed-start)
                    break
            i+=1

        resultadoInciertos = sum(tiemposBusquedaIncierta)/len(tiemposBusquedaIncierta)
        print("--- Busqueda inciertos %s segundos ---" % (resultadoInciertos))

        i=0
        random.seed(70)
        while i<100:
            while True:
                p=[]
                for d in range(k):
                    p.append(random.randint(0,10000))
                if not searchKDTree(arbolCatedra,p,r):
                    start = time.perf_counter()
                    searchKDTree(arbolCatedra,p,r)
                    elapsed = time.perf_counter()
                    tiemposBusquedaInciertaCatedra.append(elapsed-start)
                    break
            i+=1

        resultadoInciertosCatedra = sum(tiemposBusquedaInciertaCatedra)/len(tiemposBusquedaInciertaCatedra)
        print("--- Busqueda inciertos CATEDRA %s segundos ---" % (resultadoInciertosCatedra))

        resultadoTotales = (resultadoInciertos+resultadoAciertos)/2
        print("--- Busqueda total %s segundos ---" % (resultadoTotales))

        resultadoTotalesCatedra = (resultadoInciertosCatedra+resultadoAciertosCatedra)/2
        print("--- Busqueda total CATEDRA %s segundos ---" % (resultadoTotalesCatedra))
        print(" === ")
