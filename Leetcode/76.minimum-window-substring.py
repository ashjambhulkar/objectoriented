#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
import collections

class Solution:
    def minWindow(self, s, t):
        start = 0
        result = ""
        sample = set(list(t))
        count = float("inf")
        hashmap = collections.defaultdict(int)
        for end in range(len(s)):
            end_char = s[end]
            if end_char in sample:
                hashmap
                
        return result

print(Solution().minWindow("bdab", "ab"))

# @lc code=end

