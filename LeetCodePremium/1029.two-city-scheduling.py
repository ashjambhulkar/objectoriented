#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        size = len(costs)//2
        costs.sort(key= lambda x: x[0]-x[1])
        total = 0
        for i in range(size):
            total += costs[i][0]+costs[i+size][1]
        return total
# @lc code=end

