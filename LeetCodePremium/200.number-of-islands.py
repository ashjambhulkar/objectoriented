#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        result = 0
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0" 
            dfs(grid, i+1, j) 
            dfs(grid, i-1, j) 
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += dfs(grid, i, j)
        return result


# @lc code=end

