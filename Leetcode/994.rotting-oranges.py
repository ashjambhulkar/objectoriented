#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh.add((i,j))
                if grid[i][j] == 2:
                    rotten.add((i,j))
        minutes = 0
        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        while fresh:
            infected = set()
            for x in rotten:
                for y in direction:
                    i = x[0] + y[0]
                    j = x[1] + y[1]
                    
                    if (i, j) in fresh:
                        fresh.remove((i,j))
                        infected.add((i,j))
            if len(infected) == 0:
                return -1
            
            rotten = infected

            minutes += 1
        return minutes

            
        
# @lc code=end

