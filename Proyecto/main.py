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

def makeKDRTree(points, dim = 0, k = 1):
    if not points:
        return None # Empty trees are None
    elif len(points) == 1:
        return [points] # Leaf nodes have one point.
    points.sort(key = lambda p: p[dim])
    for i in range(pow(dim+1)):
        medianIndex = len(points) // 2
        median = points[medianIndex][dim]
        nextDim = (dim + 1) % len(points[medianIndex])
        left = [p for p in points if p[dim] < median]
        right = [p for p in points if p[dim] >= median]
    return [median, makeKDTree(left, nextDim), makeKDTree(right, nextDim)]


def searchKDTree(kdTree, point, dim = 0):
    if len(kdTree) == 1:
        return kdTree[0] == point
    nodeValue, left, right = kdTree
    nextDim = (dim + 1) % len(point)
    nextTree = left if point[dim] < nodeValue else right
    return searchKDTree(nextTree, point, nextDim)

#dimension = 0
#points = [[1,0],[1,1],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2],[3,3],[4,0],[4,1],[4,2],[4,3],[4,4]]
#tree = makeKDTree(points,dimension)
#print(tree)
#print(searchKDTree(tree,[2,0],dimension))
import itertools
def comparacionesDimension(array):
    return [list(e) for e in itertools.product(*[[">","<="] for x in range(len(array))])]

def crearArbol(puntos,dimension):
    if not puntos:
        return None # Empty trees are None
    elif len(puntos) == 1:
        return tuple(puntos) # Leaf nodes have one point.
    medianas = []
    for i in range(dimension):
        medianas.append(sum([x[i] for x in puntos])//len(puntos))
    print(medianas)
    auxiliares = [[] for x in range(pow(2,len(medianas)))]
    operandos = comparacionesDimension(medianas)
    operandos.sort()
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
    return resultado


print(crearArbol(
    [
        [0,0],
        [1,1],
        [2,2],
        [3,3],
        [4,4]
    ],2))
#
# array = [[1,1,1],[3,1,2]]
# mediana = [2,1,0]
# operandos = comparacionesDimension(mediana)
# print(operandos)
# for i in array:
#     for c in operandos:
#         string = []
#         for m in range(len(mediana)):
#             t = str(i[m])+" "+c[m]+" "+str(mediana[m])
#             string.append(t)
#         print("String: "+",".join(string))
#         works = True
#         for s in string:
#             if not eval(s):
#                 works = False
#                 break
#         print("Resultado: "+str(works))
#     print("====")
