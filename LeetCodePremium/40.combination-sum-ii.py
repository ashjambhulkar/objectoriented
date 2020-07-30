#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def helper(candidates, temp, target, start):
            if target == 0:
                result.append(temp[:])
            elif target > 0:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    temp.append(candidates[i])
                    helper(candidates, temp, target-candidates[i], i+1)
                    temp.pop()

        helper(candidates, [], target, 0)
        return result
                
        
# @lc code=end

