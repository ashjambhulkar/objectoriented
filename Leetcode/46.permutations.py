#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(nums, temp):
            if len(nums) == 0:
                result.append(temp[:])
            for i in range(len(nums)):
                var = nums[i]
                temp.append(var)
                nums.remove(var)
                helper(nums, temp)
                temp.pop()
                nums.insert(i, var)
        helper(nums, [])
        return result
# @lc code=end

