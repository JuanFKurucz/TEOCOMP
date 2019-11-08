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

dimension = 0
points = [[1,0],[1,1],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2],[3,3],[4,0],[4,1],[4,2],[4,3],[4,4]]
tree = makeKDTree(points,dimension)
print(tree)
#print(searchKDTree(tree,[2,0],dimension))
