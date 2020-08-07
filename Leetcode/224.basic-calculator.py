#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = 0
        operand = 0
        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            if ch.isdigit():
                operand = (10**n * int(ch)) + operand
                n += 1


# @lc code=end

