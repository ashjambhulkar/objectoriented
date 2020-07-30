#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or s == 0:
            return 0
        start = 0
        total = 0
        result = []
        for end in range(len(nums)):
            total += nums[end]
            while total >= s:
                result.append(end-start+1)
                total -= nums[start]
                start += 1
        return 0 if not result else min(result)

# @lc code=end

