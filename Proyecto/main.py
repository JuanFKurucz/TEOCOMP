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
    for i in range(pow(2,dimension)-1):
        l.append(MAYOR)
    for i in range(pow(2,dimension)):
        l.append(i)
    return l


def encontrarRecursivo(mediana,punto,inicioDimension,dimension):
    indiceCaja=0
    for indicePunto in range(dimension):
        indiceReal = (indicePunto+inicioDimension)%(len(punto))
        indiceCaja*=2
        if punto[indiceReal] < mediana[indicePunto]:
            indiceCaja+=1
        else:
            indiceCaja+=2
    return indiceCaja

"""
    n*(2^r)*r
    No se pueden tener puntos duplicados en la lista de puntos al momento de crear
"""
def crearArbol(puntos,dimension):
    puntos.sort()
    operandos = comparacionesDimension(dimension)
    return (operandos,crearArbolRecursivo(puntos,0,dimension,operandos,range(pow(2,dimension))))

def crearArbolRecursivo(puntos,inicioDimension,dimension,operandos,rangoOperandos):
    if not puntos or len(puntos)==0:
        return []
    elif len(puntos) == 1:
        return puntos
    indiceMedio = len(puntos)//2
    medianas = []
    for i in range(dimension):
        medianas.append(puntos[indiceMedio][(inicioDimension+i)%len(puntos[indiceMedio])])
    auxiliares = [[] for x in rangoOperandos]
    for i in puntos:
        auxiliares[operandos[encontrarRecursivo(medianas,i,inicioDimension,dimension)]].append(i)
    nextDimension = (inicioDimension + 1) % len(puntos[indiceMedio])
    resultado = [crearArbolRecursivo(a,nextDimension,dimension,operandos,rangoOperandos) for a in auxiliares]
    return [medianas,resultado]

"""
    (2^r)*r
"""
def buscar(arbol,punto):
    return buscarRecursivo(arbol[1],punto,0,len(arbol[1][0]),arbol[0])

def buscarRecursivo(arbol,punto,inicioDimension,dimension,operandos):
    if not arbol:
        return False
    elif len(arbol) == 1:
        return punto == arbol[0]
    else:
        return buscarRecursivo(arbol[1][operandos[encontrarRecursivo(arbol[0],punto,inicioDimension,dimension)]],punto,inicioDimension+1,dimension,operandos)

print("r,k,n,creacionArbol,creacionArbolCatedra,resultadoAciertos,resultadoAciertosCatedra,resultadoInciertos,resultadoInciertosCatedra,resultadoTotales,resultadoTotalesCatedra")
repeticiones = 100
debug = False
cantidadNumeros = [100000,500000,1000000]
repeticionesCreacion = 1
for k in [5,10,15,20]:
    random.seed(30)
    print("Creando puntos")
    start = time.perf_counter()
    maxCantidadNumeros = max(cantidadNumeros)
    puntosGeneral = {(random.randint(0, maxCantidadNumeros), random.randint(0, maxCantidadNumeros)) for i in range(maxCantidadNumeros)}
    while len(puntosGeneral) < maxCantidadNumeros:
        puntosGeneral |= {(random.randint(0, maxCantidadNumeros), random.randint(0, maxCantidadNumeros))}
    puntosGeneral = list(list(x) for x in puntosGeneral)
    elapsed = time.perf_counter()
    print("Creacion %s puntos %s"%(len(puntosGeneral),elapsed-start))
    for n in cantidadNumeros:
        print("Obteniendo puntos")
        start = time.perf_counter()
        puntos = puntosGeneral[:n]
        elapsed = time.perf_counter()
        tiempoObtenerPuntos = (elapsed-start)
        tiemposCreacionCatedra=[]
        tiemposBusquedaAciertoCatedra=[]
        tiemposBusquedaInciertaCatedra=[]
        print("Creando arbol CATEDRA")
        for i in range(repeticionesCreacion):
            start = time.perf_counter()
            arbolCatedra = makeKDTree(puntos)
            elapsed = time.perf_counter()
            tiemposCreacionCatedra.append(elapsed-start)
        print("Buscando True CATEDRA")
        for p in range(repeticiones):
            start = time.perf_counter()
            if debug:
                print(searchKDTree(arbolCatedra,puntos[p]))
            searchKDTree(arbolCatedra,puntos[p])
            elapsed = time.perf_counter()
            tiemposBusquedaAciertoCatedra.append(elapsed-start)
        print("Buscando False CATEDRA")
        i=0
        random.seed(70)
        while i<repeticiones:
            while True:
                p=[]
                for d in range(k):
                    p.append(random.randint(0,10000))
                if not searchKDTree(arbolCatedra,p):
                    if debug:
                        print(searchKDTree(arbolCatedra,p))
                    start = time.perf_counter()
                    searchKDTree(arbolCatedra,p)
                    elapsed = time.perf_counter()
                    tiemposBusquedaInciertaCatedra.append(elapsed-start)
                    break
            i+=1
        for r in range(1,6):
            tiemposCreacion=[]
            tiemposBusquedaAcierto=[]
            tiemposBusquedaIncierta=[]
            print("Creando arbol")
            for i in range(repeticionesCreacion):
                start = time.perf_counter()
                arbol = crearArbol(puntos,r)
                elapsed = time.perf_counter()
                tiemposCreacion.append(elapsed-start)
            print("Buscando True")
            for p in range(repeticiones):
                if debug:
                    print(buscar(arbol,puntos[p]))
                start = time.perf_counter()
                buscar(arbol,puntos[p])
                elapsed = time.perf_counter()
                tiemposBusquedaAcierto.append(elapsed-start)
            print("Buscando False")
            i=0
            random.seed(70)
            while i<repeticiones:
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
            resultadoAciertos = sum(tiemposBusquedaAcierto)/len(tiemposBusquedaAcierto)
            resultadoAciertosCatedra = sum(tiemposBusquedaAciertoCatedra)/len(tiemposBusquedaAciertoCatedra)
            resultadoInciertos = sum(tiemposBusquedaIncierta)/len(tiemposBusquedaIncierta)
            resultadoInciertosCatedra = sum(tiemposBusquedaInciertaCatedra)/len(tiemposBusquedaInciertaCatedra)
            resultadoTotales = (resultadoInciertos+resultadoAciertos)/2
            resultadoTotalesCatedra = (resultadoInciertosCatedra+resultadoAciertosCatedra)/2
            creacionArbol = sum(tiemposCreacion)/len(tiemposCreacion)
            creacionArbolCatedra = sum(tiemposCreacionCatedra)/len(tiemposCreacionCatedra)
            print("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(r,k,n,creacionArbol,creacionArbolCatedra,resultadoAciertos,resultadoAciertosCatedra,resultadoInciertos,resultadoInciertosCatedra,resultadoTotales,resultadoTotalesCatedra))
