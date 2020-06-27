#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        status = True
        result = ""
        for i in str(x):
            if i == "-":
                status = False
                continue

            result = i + result
        result = int(result)
        if result > pow(2, 31) or result < - pow(2, 31):
            result = 0
        if not status:
            return - (result)
        return result
        
# @lc code=end

