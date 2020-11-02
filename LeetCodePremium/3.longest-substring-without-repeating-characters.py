#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

import collections
class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        count = 0
        hashmap = collections.defaultdict(int)
        for end in range(len(s)):
            char = s[end]
            if char in hashmap:
                start = max(start, hashmap[char]+1)
            hashmap[char] = end
            count = max(count, end-start+1)
        return count

      
      
# @lc code=end

