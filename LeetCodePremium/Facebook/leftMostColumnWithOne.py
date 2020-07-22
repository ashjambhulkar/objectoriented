# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
      rows, cols = binaryMatrix.dimensions()
      smallest = cols
      for row in range(rows):
        left = 0
        right = cols - 1
        while left < right:
          mid = (left+right) // 2
          if binaryMatrix.get(row, mid) == 0:
            left = mid + 1
          else:
            right = mid
        if binaryMatrix.get(row, left) == 1:
          smallest = min(smallest, left)
      return -1 if smallest == cols else smallest
