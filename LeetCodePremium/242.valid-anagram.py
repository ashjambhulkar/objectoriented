#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = collections.defaultdict(int)
        for x in s:
            hashmap[x] += 1
        for x in t:
            hashmap[x] -= 1
            if hashmap[x] == 0:
                del hashmap[x]
        return len(hashmap) == 0
# @lc code=end

