#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        # result = []
        # def dfs(string, maximum, open, close):
        #     nonlocal result
        #     if len(string) == maximum*2:
        #         result.append(string)
        #     if open < maximum:
        #         dfs(string+"(", maximum, open+1, close)
        #     if close < open:
        #         dfs(string+")", maximum, open, close+1)
        # dfs("", n, 0, 0)
        # return result
        result = []
        def helper(open, close, string):
            nonlocal result
            if len(string) == 2 * n:
                result.append(string)
                return result
            if open < n:
                helper(open+1, close, string+"(")
            if close < open:
                helper(open, close+1, string+")")
        helper(0, 0, "")
        return result

# @lc code=end

