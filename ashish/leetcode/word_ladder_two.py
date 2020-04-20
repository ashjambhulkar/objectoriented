import collections


def helper(start, end, wordlist):
  if end not in wordlist or not end or not start or not wordlist:
    return []
  
  queue = collections.deque()
  queue.append((start, 0))
  graph = collections.defaultdict(set)
  visited = set([start])
  dist = {}
  while queue:
    node, depth = queue.popleft()
    dist[node] = depth