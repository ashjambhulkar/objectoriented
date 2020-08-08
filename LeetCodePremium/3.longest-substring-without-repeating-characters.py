#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        count = 0
        hashmap = collections.defaultdict(int)
        for end in range(len(s)):
            end_value = s[end]
            if end_value in hashmap:
                start = max(hashmap[end_value]+1, start)
            count = max(count, end-start+1)
            hashmap[end_value] = end
        return count
        
      
      
# @lc code=end

