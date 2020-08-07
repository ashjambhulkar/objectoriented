#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        
        total = sum(nums)

        if total %2 != 0:
            return False

        dp = [[False for _ in range(total//2+1)] for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True
        
        dp[0][nums[0]] = True

        for i in range(1,len(nums)):
            for j in range(1, total//2+1):
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
        
# @lc code=end

