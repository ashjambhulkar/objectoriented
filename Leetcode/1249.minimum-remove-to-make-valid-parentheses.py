#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #end stack is to track the closing parentesis after the opening parenthesis
        end = []
        #start stack to track the closing parenthesis in the start
        start = []
        # This is the final result string
        result = ""
        for i in range(len(s)):
            # checking whether the closing parenthesis is start or end 
            if s[i] == ")" and len(end) == 0:
                start.append(i)
            # else tracking the index of the opening parenthesis
            elif s[i] == "(":
                end.append(i)
            # once found the closing parenthesis delete the last found open parenthesis
            elif s[i] == ")":
                end.pop()
        # merging the start and end list
        final = start + end
        #looping over the string and checking that the index is in the final stack and skipping them while adding into the final result 
        for x in range(len(s)):
            if x not in final:
                result += s[x]

        return result
        

        
# @lc code=end

