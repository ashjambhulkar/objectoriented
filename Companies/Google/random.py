def solution(grid, topRight, bottomLeft):
  def helper(bottom, top):
    if top.x >= bottom.x or top.y >= bottom.y and sea.hasShip(top, bottom):
      if (top.x, top.y) == (bottom.x, bottom.y):
        return int(sea.hasShip(top, bottom))
      x0, y0 = bottom.x, bottom.y
      x1, y1 = top.x, top.y
      mid_x, mid_y = (x0+x1)//2, (y0+y1)//2
      return  helper(bottom,(mid_x, mid_y)) + \
              helper((mid_x+1, mid_y+1), top) + \
              helper((x0, mid_y+1), (mid_x, y1)) + helper((mid_x+1, y0), (x1, mid_y))
      
  return helper(bottomLeft, topRight)