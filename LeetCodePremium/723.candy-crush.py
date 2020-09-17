def solution(grid):
  if not grid:
    return grid
  sample = set()
  while True:
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if i > 1 and grid[i][j] == grid[i-1][j] == grid[i-2][j]:
          sample |= {(i, j), (i-1, j), (i-2, j)}
        if j > 1 and grid[i][j] == grid[i][j-1] == grid[i][j-2]:
          sample |= {(i, j), (i, j-1), (i, j-2)}

    if not sample:
      break

    for i, j in sample:
      grid[i][j] = 0

    for j in range(len(grid[0])):
      index = len(grid)-1
      for i in range(len(grid)-1, -1, -1):
        if grid[i][j]:
          grid[index][j] = grid[i][j]
          index -= 1
      for i in range(index+1):
        grid[i][j] = 0
  return grid
