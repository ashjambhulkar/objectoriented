#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for x in strs:
            b = list(x)
            b.sort()
            hashmap["".join(b)].append(x)
        return hashmap.values()
        
# @lc code=end

