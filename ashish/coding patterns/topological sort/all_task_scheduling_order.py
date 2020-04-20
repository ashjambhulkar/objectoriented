import collections


def all_task_scheduling_order(vertices, edges):
  sortedOrder = []
  
  if vertices <= 0:
    return []

  inDegree = { i:0 for i in range(vertices)}
  graph = { i:[] for i in range(vertices)}

  # create the graph
  for x in edges:
    parent, child = x[0], x[1]
    graph[parent].append(child)
    inDegree[child] += 1


  sources = collections.deque()

  # buidling graph
  for key, value in inDegree.items():
    if value == 0:
      sources.append(key)
  
  helper(graph, inDegree, sources, sortedOrder)
  

def helper(graph, inDegree, sources, sortedOrder):
  if sources:
    for vertex in sources:
      sortedOrder.append(vertex)
      sourcesForNextCall = collections.deque(sources)  # make a copy of sources
      # only remove the current source, all other sources should remain in the queue for the next call
      sourcesForNextCall.remove(vertex)
      # get the node's children to decrement their in-degrees
      for child in graph[vertex]:
        inDegree[child] -= 1
        if inDegree[child] == 0:
          sourcesForNextCall.append(child)

      # recursive call to print other orderings from the remaining (and new) sources
      helper(graph, inDegree, sourcesForNextCall, sortedOrder)

      # backtrack, remove the vertex from the sorted order and put all of its children back to consider
      # the next source instead of the current vertex
      sortedOrder.remove(vertex)
      for child in graph[vertex]:
        inDegree[child] += 1

  
  if len(sortedOrder) == len(inDegree):
    print(sortedOrder)


all_task_scheduling_order(3, [[0, 1], [1, 2]])
all_task_scheduling_order(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
all_task_scheduling_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
