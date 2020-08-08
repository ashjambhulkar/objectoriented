#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        visited = [0] * len(M)
        def dfs(grid, visited, i):
            for j in range(len(M)):
                if visited[j] == 0 and grid[i][j] == 1:
                    visited[j] =1
                    dfs(grid, visited, j)
        
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(M, visited, i)
                count += 1
        return count
        
# @lc code=end

