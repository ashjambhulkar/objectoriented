#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(nums, temp):
            result.append(temp[:])
            for i in range(len(nums)):
                temp.append(nums[i])
                helper(nums[i+1:], temp)
                temp.pop()
        helper(nums, [])
        return result
# @lc code=end

