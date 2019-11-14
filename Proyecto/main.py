import itertools
def comparacionesDimension(dimension):
    l=[list(e) for e in itertools.product(*[[">","<="] for x in range(dimension)])]
    l.sort()
    return l

"""
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

random.seed(30)
puntos = []

dimension = 2
for i in range(10000):
    while True:
        p=[]
        for d in range(dimension):
            p.append(random.randint(0,40000))
        if p not in puntos:
            puntos.append(p)
            break
arbol = crearArbol(puntos,dimension)

print(arbol)
print("======BUSQUEDA=======")

print(buscar(arbol,[16,3]))
