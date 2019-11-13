import itertools
def comparacionesDimension(dimension):
    l=[list(e) for e in itertools.product(*[[">","<="] for x in range(dimension)])]
    l.sort()
    return l

def crearArbol(puntos,dimension):
    if not puntos:
        return None # Empty trees are None
    elif len(puntos) == 1:
        return puntos # Leaf nodes have one point.
    medianas = []
    for i in range(dimension):
        medianas.append(sum([x[i] for x in puntos])//len(puntos))
    print(medianas)
    auxiliares = [[] for x in range(pow(2,len(medianas)))]
    operandos = comparacionesDimension(len(medianas))
    for i in puntos:
        print("======")
        indice = 0
        for c in operandos:
            string = []
            for m in range(len(medianas)):
                t = str(i[m])+" "+c[m]+" "+str(medianas[m])
                string.append(t)
            works = True
            print(string)
            for s in string:
                if not eval(s):
                    works = False
                    break
            print(works)
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

arbol = crearArbol(
[
    [0,0],
    [2,2],
    [2,4],
    [3,3],
    [4,4],
    [5,5]
],2)

print(arbol)
print("======BUSQUEDA=======")

print(buscar(arbol,[0,0]))
print(buscar(arbol,[2,2]))
print(buscar(arbol,[2,4]))
print(buscar(arbol,[3,3]))
print(buscar(arbol,[4,4]))
print(buscar(arbol,[5,5]))
