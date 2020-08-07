#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(candidates, temp, target, start):
            if target == 0:
                result.append(temp[:])
            elif target > 0:
                for i in range(start, len(candidates)):
                    temp.append(candidates[i])
                    helper(candidates, temp, target-candidates[i], i)
                    temp.pop()
        helper(candidates, [], target, 0)
        return result
        
# @lc code=end

