#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(int(math.sqrt(n))+1)]
        
        dp = [0] + [float("inf")] * (n)

        for sqr in squares:
            for x in range(sqr, n+1):
                dp[x] = min(dp[x], dp[x-sqr]+1)
        return dp[-1]

# @lc code=end

