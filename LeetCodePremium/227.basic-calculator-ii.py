#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        total = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                total += total*10 + int(s[i])
            if s[i] in "-+/*" or i == len(s)-1:
                if sign == "+":
                    stack.append(total)
                elif sign == "-":
                    stack.append(-total)
                elif sign == "*":
                    stack.append(stack.pop()*total)
                elif sign == "/":
                    stack.append(int(stack.pop()/total))
                total = 0
                sign = s[i]
        return sum(stack)
  
# @lc code=end

