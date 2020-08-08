#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # status = True
        # result = ""
        # for i in str(x):
        #     if i == "-":
        #         status = False
        #         continue

        #     result = i + result
        # result = int(result)
        # if result > pow(2, 31) or result < - pow(2, 31):
        #     result = 0
        # if not status:
        #     return - (result)
        # return result
        sign = 0
        if x < 0:
            sign = 1
            x = -1 * x
        x = str(x)
        x = int(x[::-1])
        if sign == 1:
            x = -1 * x
        if x > pow(2, 31) or x < - pow(2, 31):
            return 0
        return x
        

        
# @lc code=end

