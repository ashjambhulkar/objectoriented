import collections


def task_scheduling(vertices, edges):
  sortedOrder = []

  if vertices <= 0:
    return False

  graph = { i : []  for i in range(vertices)}
  inDegree  = { i: 0 for i in range(vertices)}

  # create the graph
  for x in edges:
    parent, child = x[0], x[1]
    graph[parent].append(child)
    inDegree[child] += 1

  queue = collections.deque()
  for key, value in inDegree.items():
    if value == 0:
      queue.append(key)

  while queue:
    vertex = queue.popleft()
    sortedOrder.append(vertex)
    for x in graph[vertex]:
      inDegree[x] -= 1
      if inDegree[x] == 0:
        queue.append(x)
  
  return len(sortedOrder) == vertices
    

print(task_scheduling(3, [[0, 1], [1, 2]]))
print(task_scheduling(3, [[0, 1], [1, 2], [2, 0]]))
print(task_scheduling(6, [[0, 4], [1, 4], [3, 2], [1, 3]]))



