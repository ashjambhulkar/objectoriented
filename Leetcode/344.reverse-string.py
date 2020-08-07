#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(s,l=0, r = len(s)-1 ):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            helper(s, l+1, r-1)

        helper(s)
        return s

        
# @lc code=end

