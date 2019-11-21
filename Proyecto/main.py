import time
import itertools
import random

MAYOR = None
def searchKDTree(kdTree, point, dim = 0):
    if len(kdTree) == 1:
        return kdTree[0] == point
    nodeValue, left, right = kdTree
    nextDim = (dim + 1) % len(point)
    nextTree = left if point[dim] < nodeValue else right
    return searchKDTree(nextTree, point, nextDim)

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

def comparacionesDimension(dimension):
    l=[]
    for i in range(pow(dimension,2)-1):
        l.append(MAYOR)
    for i in range(pow(dimension,2)):
        l.append(i)
    return l


"""
    n*(2^r)*r
    No se pueden tener puntos duplicados en la lista de puntos al momento de crear
"""
def crearArbol(puntos,dimension):
    operandos = comparacionesDimension(dimension)
    return crearArbolRecursivo(puntos,dimension,operandos,range(len(operandos)),range(dimension))

def crearArbolRecursivo(puntos,dimension,operandos,rangoOperandos,rangoDimension):
    if not puntos:
        return []
    elif len(puntos) == 1:
        return puntos
    largoPuntos = len(puntos)
    medianas = [sum([x[i] for x in puntos])//largoPuntos for i in rangoDimension]
    auxiliares = [[] for x in rangoOperandos]
    for i in puntos:
        m=0
        p=0
        while p<dimension:
            m=2*m+2
            if i[p] > medianas[p]:
                m-=1
            p+=1
        auxiliares[m].append(i)
    resultado = [crearArbolRecursivo(a,dimension,operandos,rangoOperandos,rangoDimension) for a in auxiliares]
    return [medianas,resultado]

"""
    (2^r)*r
"""
def buscar(arbol,punto):
    if punto == None:
        return False
    return buscarRecursivo(arbol,punto)

def buscarRecursivo(arbol,punto):
    if not arbol:
        return False
    elif len(arbol) == 1:
        return punto == arbol[0]
    m=0
    p=0
    while p<r:
        m=2*m+2
        if punto[p] > arbol[0][p]:
            m-=1
        p+=1
    return buscarRecursivo(arbol[1][m],punto)

r=3
repeticiones = 100
debug = False
for k in [5,10,15,20]:
    random.seed(30)
    print("Start "+str(k)+" using "+str(r))
    cantidadNumeros = [100000,500000,1000000]
    puntosGeneral = []
    start = time.perf_counter()
    n=max(cantidadNumeros)
    pDim = []
    for d in range(k):
        choices = list(range(n))
        random.shuffle(choices)
        pDim.append(choices)
    for i in range(n):
        p=[]
        for d in range(k):
            p.append(pDim[d][i])
        puntosGeneral.append(p)
    elapsed = time.perf_counter()
    print("--- Generacion puntos %s segundos ---" % (elapsed-start))

    for n in cantidadNumeros:
        print("N "+str(n))
        start = time.perf_counter()
        puntos = puntosGeneral[:n]
        elapsed = time.perf_counter()
        print("--- Obtener "+str(len(puntos))+" puntos %s segundos ---" % (elapsed-start))
        tiemposCreacion=[]
        for i in range(repeticiones):
            start = time.perf_counter()
            arbol = crearArbol(puntos,r)
            elapsed = time.perf_counter()
            tiemposCreacion.append(elapsed-start)
        print("--- Creacion arbol %s segundos ---" % (sum(tiemposCreacion)/len(tiemposCreacion)))
        tiemposCreacionCatedra=[]
        for i in range(repeticiones):
            start = time.perf_counter()
            arbolCatedra = makeKDTree(puntos,r)
            elapsed = time.perf_counter()
            tiemposCreacionCatedra.append(elapsed-start)
        print("--- Creacion arbol CATEDRA %s segundos ---" % (sum(tiemposCreacionCatedra)/len(tiemposCreacionCatedra)))
        #r-=1
        tiemposBusquedaAcierto=[]
        tiemposBusquedaIncierta=[]
        print("Inicio busqueda aciertos")
        for p in range(repeticiones):
            if debug:
                print(buscar(arbol,puntos[p]))
            start = time.perf_counter()
            buscar(arbol,puntos[p])
            elapsed = time.perf_counter()
            tiemposBusquedaAcierto.append(elapsed-start)
        resultadoAciertos = sum(tiemposBusquedaAcierto)/len(tiemposBusquedaAcierto)
        print("--- Busqueda aciertos %s segundos ---" % (resultadoAciertos))

        tiemposBusquedaAciertoCatedra=[]
        tiemposBusquedaInciertaCatedra=[]
        for p in range(repeticiones):
            start = time.perf_counter()
            if debug:
                print(searchKDTree(arbolCatedra,puntos[p],r))
            searchKDTree(arbolCatedra,puntos[p],r)
            elapsed = time.perf_counter()
            tiemposBusquedaAciertoCatedra.append(elapsed-start)
        resultadoAciertosCatedra = sum(tiemposBusquedaAciertoCatedra)/len(tiemposBusquedaAciertoCatedra)
        print("--- Busqueda aciertos CATEDRA %s segundos ---" % (resultadoAciertosCatedra))

        print("Inicio busqueda inciertos")
        i=0
        random.seed(70)
        while i<repeticiones:#0:
            while True:
                p=[]
                for d in range(k):
                    p.append(random.randint(0,10000))
                if not buscar(arbol,p):
                    if debug:
                        print(buscar(arbol,p))
                    start = time.perf_counter()
                    buscar(arbol,p)
                    elapsed = time.perf_counter()
                    tiemposBusquedaIncierta.append(elapsed-start)
                    break
            i+=1

        resultadoInciertos = sum(tiemposBusquedaIncierta)/len(tiemposBusquedaIncierta)
        print("--- Busqueda inciertos %s segundos ---" % (resultadoInciertos))

        i=0
        random.seed(70)
        while i<repeticiones:
            while True:
                p=[]
                for d in range(k):
                    p.append(random.randint(0,10000))
                if not searchKDTree(arbolCatedra,p,r):
                    if debug:
                        print(searchKDTree(arbolCatedra,p,r))
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
