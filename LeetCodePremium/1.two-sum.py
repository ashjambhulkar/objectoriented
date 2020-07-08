#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        start = 0
        end = len(nums)-1
        while start < end:
            sample = nums[start] + nums[end]
            if sample == target:
                return [start, end]
            elif sample < target:
                start += 1
            else:
                end -= 1
        

        
# @lc code=end

