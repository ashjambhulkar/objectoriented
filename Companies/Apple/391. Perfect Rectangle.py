import itertools

def helper(self, rectangles):
  x1, y1, x2, y2 = float("inf"), float("inf"), float("-inf"), float("-inf")
  area = 0
  for rect in rectangles:
    x1 = min(x1, rect[0])
    y1 = min(y1, rect[1])
    x2 = max(x2, rect[2])
    y2 = max(y2, rect[3])

    area += (rect[3]-rect[1]) * (rect[2]-rect[0])
    hashset = set()
    for x, y in itertools.product([rect[0], rect[2]],[rect[1],rect[3]]):
      if (x, y) in hashset:
        hashset.remove((x,y))
      else:
        hashset.add((x,y))
    return len(hashset) == 4 and area == (x2-x1) * (y2-y1) and all((x,y) in hashset for x, y in itertools.product([x1, x2], [y1, y2]))

