import collections


def topological_sort(vertices, edges):
  sortedOrder = []
  
  if vertices <= 0:
    return sortedOrder
  
  inDegree = { i: 0  for i in range(vertices)}
  graph = { i: [] for i in range(vertices)}

  # building the graph and indegree(incoming arrows)
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)
    inDegree[child] += 1

  # find all the sources with zero indegree
  sources = collections.deque()
  for key, value in inDegree.items():
    if value == 0:
      sources.append(key)

  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)
  
  # topological sort is not possible as the graph has a cycle
  if len(sortedOrder) != vertices:
    return []

  return sortedOrder
  

print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
print(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
print(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))



def helper(vertices ,edges):
  graph = collections.defaultdict(list)
  inchild = collections.defaultdict(int)

  for edge in edges:
    graph[edge[0]].append(edge[1])
    inchild[edge[1]] += 1

  start = collections.deque()

  for key, value in inchild.item():
    start.append(value)
  
  visited = set()
  result = []
  while start:
    node =  start.popleft()
    result.add(node)
    for x in graph[node]:
      inchild[node] -= 1
      if inchild[node] == 0:
        start.append(node)
    
    if len(result) != vertices:
      return []
    return result
  
