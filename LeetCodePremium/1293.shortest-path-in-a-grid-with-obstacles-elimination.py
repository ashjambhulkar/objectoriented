#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start

# Time Complexity
# O(m*n*k) time complexity
# This is because for every cell(m*n), in the worst case we have to put that cell into the queue/bfs k times.

# Runtime: 68 ms, faster than 33.33 % of Python3 online submissions

# Space Complexity
# O(m*n*k) space complexity
# This is because for every cell(m*n), in the worst case we have to put that cell into the queue/bfs k times which means we need to worst case store all of those steps/paths in the visited set.

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        if k > len(grid[0])-1 + len(grid)-1:
            return len(grid[0])-1 + len(grid)-1

        queue = collections.deque([(0,0,0,k)])
        visited = set([(0,0,k)])

        while queue:
            x, y, depth, remain = queue.popleft()
            for p, q in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if p >= 0 and p < len(grid) and q >= 0 and q < len(grid[0]):
                    if grid[p][q] == 1 and remain > 0 and (p,q,remain-1) not in visited:
                        visited.add((p,q,remain-1))
                        queue.append((p,q,depth+1, remain-1))
                    if grid[p][q] == 0 and (p,q,remain) not in visited:
                        if p == len(grid)-1 and q == len(grid[0])-1:
                            return depth+1
                        visited.add((p,q,remain))
                        queue.append((p,q,depth+1, remain))       
        return -1
                

# @lc code=end

