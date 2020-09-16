#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
# "deeedbbcccbdaa"
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["#",0]]
        for x in s:
            if stack[-1][0] == x:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([x,1])
        result = ""
        for x, y in stack:
            result += x * y
        return result

        
# @lc code=end

