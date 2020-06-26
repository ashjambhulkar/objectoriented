#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def helper(target, nums, start):
            last = len(nums)-1
            while start < last:
                temp = nums[start] + nums[last]
                if temp == target:
                    result.append([-target, nums[start], nums[last]])
                    start += 1
                    last -= 1
                    while start < last and nums[start] == nums[start-1]:
                        start += 1
                    while start < last and nums[last] == nums[last+1]:
                        last -= 1
                elif temp < target:
                    start += 1
                else:
                    last -= 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            helper(-nums[i], nums, i+1)
        return result
        
            
# @lc code=end

