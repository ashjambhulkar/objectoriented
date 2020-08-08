#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty:
                return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False
# @lc code=end

