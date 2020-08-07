#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], w: int) -> bool:
        result = collections.Counter(hand)
        while result:
            x = min(result)
            for i in range(x, x+w):
                v = result[i]
                if not v: return False
                result[i] -=1
                if result[i] == 0:
                    del result[i]
        return True

# @lc code=end

