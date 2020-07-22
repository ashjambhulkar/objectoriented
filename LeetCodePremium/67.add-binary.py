#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        small = a
        large = b
        if len(a) > len(b):
            large = a
            small = b
        for _ in range(len(large)-len(small)):
            small = "0" + small
        carry = 0
        result = ""
        for i in range(len(small)-1, -1, -1):
            temp = int(small[i]) + int(large[i]) + carry
            carry = 0
            if temp >= 2:
                temp -= 2
                carry = 1
            result = str(temp) + result
        if carry:
            result = str(carry) + result
        return result

      
# @lc code=end

