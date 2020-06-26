#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        second = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+second] == needle:
                    return i
        return -1      
        
# @lc code=end

