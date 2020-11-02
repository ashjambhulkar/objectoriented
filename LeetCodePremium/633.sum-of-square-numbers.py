#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lo = 0
        hi = int(math.sqrt(c))
        while lo <= hi:
            total = lo*lo + hi*hi
            if total == c:
                return True
            if total < c:
                lo += 1
            else:
                hi -= 1
        return False
        
# @lc code=end

