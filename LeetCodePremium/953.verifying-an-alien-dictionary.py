#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        state = collections.defaultdict(int)
        
        for i in range(order):
            state[order[i]] = i
        
        for x in words:
            
        
# @lc code=end

