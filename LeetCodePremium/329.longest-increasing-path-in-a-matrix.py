#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        result = 1
        cache = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                result = max(result, self.dfs(matrix, i, j, cache, rows, cols))
        return result


    def dfs(self, matrix, x, y, cache, rows, cols):
        if cache[x][y] != 0:
            return cache[x][y]
        dirn = [[0,1], [0,-1], [1,0], [-1,0]]
        max_length = 1
        for d in dirn:
            dx, dy = x + d[0], y + d[1]

            if dx < 0  or dx >= rows or dy < 0 or dy >= cols or matrix[dx][dy] <= matrix[x][y]:
                continue
            max_length = max(max_length, 1 + self.dfs(matrix, dx, dy, cache, rows, cols))
        cache[x][y] = max_length
        return max_length


# matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
# print(Solution().longestIncreasingPath(matrix))
# @lc code=end

