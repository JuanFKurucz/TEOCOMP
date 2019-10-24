def makeKDTree(points, dim = 0):
  if not points:
    return None
  elif len(points) == 1:
    return tuple(points)
  points.sort(key = lambda p: p[dim])
  medianIndex = len(points) // 2
  median = points[medianIndex][dim]
  nextDim = (dim + 1) % len(points[medianIndex])
  left = points[:medianIndex]
  right = points[medianIndex:]
  return (median, makeKDTree(left, nextDim), makeKDTree(right, nextDim))

def searchKDTree(kdTree, point, dim = 0):
  if len(kdTree) == 1:
    return kdTree[0] == point
  nodeValue, left, right = kdTree
  nextDim = (dim + 1) % len(point)
  nextTree = left if point[dim] < nodeValue else right
  return searchKDTree(nextTree, point, nextDim)

kdTree1 = makeKDTree([(1,9), (2,3), (3,7), (4,1), (5,4), (6,8), (7,2), (7,9), (8,8), (9,6)])

print(kdTree1)
print(searchKDTree(kdTree1, (1,9)))
print(searchKDTree(kdTree1, (9,6)))
print(searchKDTree(kdTree1, (5,4)))
print(searchKDTree(kdTree1, (2,6)))
