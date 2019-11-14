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
            string = []
            for m in range(len(medianas)):
                t = str(i[m])+" "+c[m]+" "+str(medianas[m])
                string.append(t)
            works = True
            for s in string:
                if not eval(s):
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
def buscar(arbol,punto):
    if arbol == None:
        return False
    if len(arbol) == 1:
        return punto == arbol[0]
    operandos = comparacionesDimension(len(punto))
    mediana = arbol[0]
    indice = 0
    for c in operandos:
        string = []
        for m in range(len(mediana)):
            t = str(punto[m])+" "+c[m]+" "+str(mediana[m])
            string.append(t)
        works = True
        for s in string:
            if not eval(s):
                works = False
                break
        if works:
            return buscar(arbol[1][indice],punto)
        indice+=1
    return False

import random

for k in [5,10,15,20]:
    random.seed(30)
    print("Start "+str(k))
    start = time.perf_counter()
    puntos = []
    for n in [10]:#[100000,500000,1000000]:
        for i in range(n):
            while True:
                p=[]
                for d in range(k):
                    p.append(random.randint(0,10000))
                if p not in puntos:
                    puntos.append(p)
                    break
    elapsed = time.perf_counter()
    print("--- Generacion puntos %s segundos ---" % (elapsed-start))
    start = time.perf_counter()
    arbol=crearArbol(puntos,k)
    elapsed = time.perf_counter()
    print("--- Creacion arbol %s segundos ---" % (elapsed-start))

    tiemposBusquedaAcierto=[]
    tiemposBusquedaIncierta=[]
    print("Inicio busqueda aciertos")
    for p in puntos:
        start = time.perf_counter()
        buscar(arbol,p)
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
            print(p)
            print(p in puntos)
            if p not in puntos:
                start = time.perf_counter()
                buscar(arbol,p)
                elapsed = time.perf_counter()
                tiemposBusquedaIncierta.append(elapsed-start)
                break
        i+=1
    print("--- Busqueda inciertos %s segundos ---" % (sum(tiemposBusquedaIncierta)/len(tiemposBusquedaIncierta)))
    print("--- Busqueda total %s segundos ---" % ((sum(tiemposBusquedaAcierto)+sum(tiemposBusquedaIncierta))/(len(tiemposBusquedaIncierta)+len(tiemposBusquedaAcierto))))


#print("======BUSQUEDA=======")
#print(buscar(arbol,[4760,10479]))
