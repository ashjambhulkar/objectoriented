#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        small = num1
        large = num2
        if len(num1) > len(num2):
            large = num1
            small = num2
        for _ in range(len(large) - len(small)):
            small = "0" + small
        carry = 0
        result = ""
        for x in range(len(large)-1,-1,-1):
            temp = int(small[x]) + int(large[x]) + carry
            carry = 0
            if temp > 9:
                temp -= 10
                carry = 1
            result = str(temp) + result
        if carry:
            result = str(carry) + result
        return result
# @lc code=end

