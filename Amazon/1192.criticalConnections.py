import collections

# This is an iteration of tarjen algorithm
def criticalConnections(n ,connections):
  def dfs(rank, curr, prev):
    # low checking that current node is visited or not
    # result is for the collection of the articulation point
    low[curr], result = rank, []

    for neighbor in edges[curr]:
      # the node is already visited and its parent node therefore we can skip this
      if neighbor == prev: continue
      # if the node is not visited
      if not low[neighbor]:
        #then perform the dfs for the new node exploring its neighbors
        result += dfs(rank + 1, neighbor, curr)
      #once visit the visited node update low value with min value of current node with the already visited node
      low[curr] = min(low[curr], low[neighbor])
      #if low value is greater or equal than the rank of high value then thats the articualtion point append it 
      if low[neighbor] >= rank + 1:
          result.append([curr, neighbor])
    return result

  # low - > low values
  low, edges = [0] * n, collections.defaultdict(list)
  for u, v in connections:
      edges[u].append(v)
      edges[v].append(u)
  # rank = 1 it is just depth
  # curr is the curent node
  # prev is the previous node here -1 taken for dummy
  return dfs(1, 0, -1)
  
