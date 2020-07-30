#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s):
        result = []
        def helper(string, temp):
            if len(string) == 0:
                result.append(temp[:])
            for i in range(len(string)):
                var = string[:i+1]
                if var == var[::-1]:
                    temp.append(var)
                    print(temp)
                    helper(string[i+1:], temp)
                    print(temp)
                    temp.pop()
        helper(s, [])
        return result

Solution().partition("aab")
        
# @lc code=end

