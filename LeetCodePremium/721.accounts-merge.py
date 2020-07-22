#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        result = collections.defaultdict(set)
        for x in accounts:
            result[x[0]].add(set(x[1:]))
        print(result)
        
# @lc code=end

