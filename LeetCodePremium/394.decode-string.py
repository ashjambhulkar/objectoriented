#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s):
        stack = []
        for x in s:
            if x == "]":
                temp = stack.pop()
                middle = ""
                while temp != "[":
                    middle = temp + middle
                    temp = stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + str(num)
                num = int(num)
                stack.append(middle*num)
            else:
                stack.append(x)
        result = ""
        for x in stack:
            result += x
        return result  


print(Solution().decodeString("2[abc]3[cd]ef"))

            
        
# @lc code=end

