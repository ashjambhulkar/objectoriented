import collections


def Conn(edges):
  graph = collections.defaultdict(set)

  def dfs(source, destination):
    if source not in seen:
      seen.add(source)
      if source == destination:
        return True
      return any(dfs(nei, destination) for nei in graph[source])

  for u, v in edges:
    seen = set()
    if u in graph and v in graph and dfs(u, v):
      return u, v
    graph[u].add(v)
    graph[v].add(u)


edges = [[1, 2], [1, 3], [2, 3]]
print(Conn(edges))
