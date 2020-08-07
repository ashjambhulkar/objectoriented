import collections

# The depth first search approach
def Conn(edges):
  #we created the graph first for the edges
  graph = collections.defaultdict(set)

  def dfs(source, target):
    if source not in visited:
      visited.add(source)
      # if we the source reached the target by using depth first search
      if source == target:
        return True
      #here any means if there is even a single element which is true in the array then it returns true otherwise false
      #we are performing dfs like first taking key as a source and then performing the dfs on value taking value as key so its like loop in the hashmap
      return any(dfs(source, target) for source in graph[source])

  #then we add the source and destination on both the side into the graph 
  
  for u, v in edges:
    #the visited parameter for the dfs to not visit the same element again and again.
    visited = set()
    #if source and target is in the graph and also there is a path to reach the source to the target then the current path is redundant and we can remove that path
    if u in graph and v in graph and dfs(u, v):
      return u, v
    # otherwise add the edges
    graph[u].add(v)
    graph[v].add(u)


edges = [[1,2], [1,3], [2,3]]
print(Conn(edges))


# The union find approach with rank

class DSU:
  # here we have created the parent array and rank array
  def __init__(self):
    self.parent = list(range(1001))
    self.rank = [0] * 1001

  def find(self, x):
    # if the parent element is equal to the index element that means the element is root element otherwise perform recursion till we reach to the element where the parent is equal to the index
    if self.parent[x] != x:
      self.find(self.parent[x])
    return x

  def union(self, x, y):
    # find the parent of both the element
    xr, yr = self.find(x), self.find(y)
    # if parent of both the element are same that means its cycle as both are from the same group therefore return false
    if xr == yr:
      return False
    # assign value to the element whose rank is lower 
    elif self.rank[xr] < self.rank[yr]:
      self.parent[xr] = yr
    elif self.rank[xr] > self.rank[yr]:
      self.parent[yr] = xr
    else:
      # otherwise assign make any element as root element and increae the assigned element rank by one
      self.parent[yr] = xr
      self.rank[xr] += 1
    return True

class Solution:
  def cir(self, edges):
    dsu = DSU()
    for edge in edges:
      if not dsu.union(*edge):
        # return the edge which creates cycle as tree does not have cycle
        return edge


# The union find approach without using rank
class DSU2:
  def __init__(self):
    self.parent = list(range(1001))
  
  def find(self, x):
    if self.parent[x] != x:
      x = self.find(self.parent[x])
    return x
  
  def union(self, x, y):
    xr, yr = self.find(x), self.find(y)
    self.parent[xr] = yr
