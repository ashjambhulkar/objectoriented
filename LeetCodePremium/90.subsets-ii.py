#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def helper(nums, temp):
            result.append(temp[:])
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                helper(nums[i+1:], temp)
                temp.pop()
        helper(nums, [])
        return result
        
# @lc code=end

