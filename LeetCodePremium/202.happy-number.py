#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n != 1:
            temp = 0
            for x in (str(n)):
                temp += int(x)**2
            if temp in hashset:
                return False
            hashset.add(temp)
            n = temp
        return True
        
# @lc code=end

