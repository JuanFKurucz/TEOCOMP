import time
import itertools
def comparacionesDimension(dimension):
    l=[list(e) for e in itertools.product(*[[">","<="] for x in range(dimension)])]
    l.sort()
    return l

"""
    n*(2^r)*r
    No se pueden tener puntos duplicados en la lista de puntos al momento de crear
"""
def crearArbol(puntos,dimension):
    if not puntos:
        return None # Empty trees are None
    elif len(puntos) == 1:
        return puntos # Leaf nodes have one point.
    medianas = []
    for i in range(dimension):
        medianas.append(sum([x[i] for x in puntos])//len(puntos))
    auxiliares = [[] for x in range(pow(2,len(medianas)))]
    operandos = comparacionesDimension(len(medianas))
    for i in puntos:
        indice = 0
        for c in operandos:
            works = True
            for m in range(len(medianas)):
                if c[m] == ">":
                    if i[m] <= medianas[m]:
                        works = False
                        break
                else:
                    if i[m] > medianas[m]:
                        works = False
                        break
            if works:
                auxiliares[indice].append(i)
            indice+=1
    resultado = []
    for a in auxiliares:
        resultado.append(crearArbol(a,dimension))
    return (medianas,resultado)

"""
    (2^r)*r
"""
def buscar(arbol,punto,r):
    if arbol == None:
        return False
    if len(arbol) == 1:
        return punto == arbol[0]
    operandos = comparacionesDimension(r)
    medianas = arbol[0]
    indice = 0
    for c in operandos:
        works = True
        for m in range(len(medianas)):
            if c[m] == ">" and not (punto[m] > medianas[m]):
                works = False
                break
            elif c[m] == "<=" and not (punto[m] <= medianas[m]):
                works = False
                break
        if works:
            return buscar(arbol[1][indice],punto,r)
        indice+=1
    return False

import random

r=3
for k in [20]:
    print("Start "+str(k))
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
        for p in puntos:
            start = time.perf_counter()
            buscar(arbol,p,r)
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
