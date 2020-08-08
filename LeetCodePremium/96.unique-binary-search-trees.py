#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        g = [0] * (n+1)
        g[0], g[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                print(g)
                g[i] += g[j-1] * g[i-j]
        
        return g[n]
# @lc code=end

