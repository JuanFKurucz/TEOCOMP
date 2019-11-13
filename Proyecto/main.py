import itertools
def comparacionesDimension(dimension):
    return [list(e) for e in itertools.product(*[[">","<="] for x in range(dimension)])]

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
    operandos.sort()
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


print(crearArbol(
    [
        [2,2],
        [4,4]
    ],2))
