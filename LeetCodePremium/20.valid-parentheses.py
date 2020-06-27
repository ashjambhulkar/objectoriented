#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { "}": "{", "]": "[", ")": "("} 
        for x in s:
            if x in hashmap:
                if stack and stack[-1] == hashmap[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return len(stack) == 0
 # @lc code=end

