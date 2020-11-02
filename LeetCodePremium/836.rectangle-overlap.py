#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a, b = rec1, rec2

        if a[2] <= b[0] or a[3] <= b[1] or a[0] >= b[2] or a[1] >= b[3]:
          return False
        return True
        
# @lc code=end

