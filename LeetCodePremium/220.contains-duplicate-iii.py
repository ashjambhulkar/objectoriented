#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)-1):
            temp = abs(t - nums[i])
            for j in range(i+1, len(nums)):
                if nums[j] <= temp and j-i <= k:
                    return True
        return False
        
# @lc code=end

