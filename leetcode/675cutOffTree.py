import collections


def helper(grid):
  pass


def bfs(forest, sr, sc, tr, tc):
  row, col = len(forest), len(forest[0])
  queue = collections.deque((sr,sc, 0))
  visited = {(sr,sc)}
  while queue:
    r, c, d = queue.popleft()
    if r == tr and c == tc:
      return d
    
    for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
      if (0<= nr < row and 0 <= nc < col and forest[nr][nc] and (nr,nc) not in seen):
        visited.add((nr,nc))
        queue.append((nr, nc, d+1))

  return -1


  