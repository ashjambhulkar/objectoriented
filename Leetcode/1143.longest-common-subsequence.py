#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        row = len(text2)
        col = len(text1)

        dp = [[0] * (col+1)] * (row+1)

        for i in range(1, row+1):
          for j in range(1, col+1):
            if text2[i-1] == text1[j-1]:
              dp[i][j] = dp[i-1][j-1] + 1
            else:
              dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


# @lc code=end

