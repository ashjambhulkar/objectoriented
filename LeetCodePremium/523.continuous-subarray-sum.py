#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        result = collections.defaultdict(int)

        total = 0
        result[0] = -1

        for i in range(len(nums)):
            total += nums[i]
            if k != 0:
                total %= k
            if total in result:
                if i-result[total] > 1:
                    return True
            else:
                result[total] = i
        return False


            
# @lc code=end

