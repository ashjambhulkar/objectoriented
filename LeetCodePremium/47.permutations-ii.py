#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def helper(nums, temp):
            if len(nums) == 0:
                result.append(temp[:])
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                var = nums[i]
                temp.append(var)
                nums.remove(var)
                helper(nums, temp)
                temp.pop()
                nums.insert(i, var)
        helper(nums, [])
        return result
        
# @lc code=end

