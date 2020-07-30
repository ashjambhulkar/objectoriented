#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0

#Here the most important point is checking the stack and then rest
#stack and i < len(popped) and stack[-1] == popped[i]
#like this because in case of [1,0][1,0] the stack will get empty and will throw and error if not checked the stack in first hand
#the best solution has this perhaps
#stack and i < len(popped) and stack[-1] == popped[i]
#so I changed my code accordingly


#top voted explanation
# O(n) Space: O(n) Algorithm: try to simulate the result. If it is possible, the final stack should be empty so we can return the “not” of it. At every pushed value, append to the stack, keeping an index to traverse the popped stack. If you encounter that the top of the stack equals a pop candidate, keep popping from the stack. At the end, we expect a completely empty stack if this was a valid combination of inputs.

# @lc code=end

