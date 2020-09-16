#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        total = float("-inf")
        for x in nums:
            temp += x
            temp = max(temp, x)
            total = max(total, temp)
        return total
        
# @lc code=end

