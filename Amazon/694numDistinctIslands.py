def helper(grid):
  if not grid:
    return

  shapes = set()

  def dfs(grid, i, j, p, q):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
      return 

    grid[i][j] = 0

    shape.add((i-p, j-q))
    dfs(grid, i+1, j, p, q)
    dfs(grid, i-1, j, p, q)
    dfs(grid, i, j+1, p, q)
    dfs(grid, i, j-1, p, q)

  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 1:
        shape = set()
        dfs(grid, i, j, i, j)
        if shape:
          shapes.add(frozenset(shape))
  return len(shapes)
